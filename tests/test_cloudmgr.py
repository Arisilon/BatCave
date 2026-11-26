"""Unit tests for the cloudmgr module."""

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name,protected-access
# flake8: noqa

from unittest import main, TestCase
from unittest.mock import MagicMock, patch

from docker import DockerClient
from docker.errors import ImageNotFound

from batcave.cloudmgr import Cloud, CloudError, CloudType, Container, Image, validate_type


def docker_client_mock() -> MagicMock:
    """Create a Docker client mock that passes isinstance checks used by cloudmgr."""
    return MagicMock(spec=DockerClient)


class TestValidateType(TestCase):
    def test_valid_cloud_types(self):
        for cloud_type in CloudType:
            self.assertIsNone(validate_type(cloud_type))

    def test_invalid_cloud_type(self):
        with self.assertRaises(CloudError) as context:
            validate_type('invalid')
        self.assertEqual(CloudError.INVALID_TYPE.code, context.exception.code)


class TestCloud(TestCase):
    def test_context_manager_enter_returns_self(self):
        cloud = Cloud(CloudType.local, login=False)
        with cloud as context:
            self.assertIs(context, cloud)

    def test_context_manager_exit_returns_false(self):
        cloud = Cloud(CloudType.local, login=False)
        self.assertFalse(cloud.__exit__(None, None, None))

    def test_initialization_stores_auth_and_type(self):
        cloud = Cloud(CloudType.dockerhub, auth=('user', 'password'), login=False)
        self.assertEqual(cloud.auth, ('user', 'password'))
        self.assertIs(cloud.type, CloudType.dockerhub)
        self.assertFalse(cloud.client)

    def test_login_local_creates_docker_client(self):
        client = docker_client_mock()
        with patch('batcave.cloudmgr.DockerClient', return_value=client):
            cloud = Cloud(CloudType.local)
        self.assertIs(cloud.client, client)
        client.login.assert_not_called()

    def test_login_dockerhub_creates_and_logs_in_to_client(self):
        client = docker_client_mock()
        with patch('batcave.cloudmgr.DockerClient', return_value=client):
            _unused_cloud = Cloud(CloudType.dockerhub, auth=('user', 'password'))
        client.login.assert_called_once_with('user', 'password')

    def test_exec_gcloud_forwards_arguments(self):
        cloud = Cloud(CloudType.gcloud, login=False)
        with patch('batcave.cloudmgr.gcloud', return_value='result') as mock_gcloud:
            result = cloud.exec('projects', 'list', format='json')
        mock_gcloud.assert_called_once_with('projects', 'list', format='json')
        self.assertEqual(result, 'result')

    def test_exec_invalid_operation_for_local(self):
        cloud = Cloud(CloudType.local, login=False)
        with self.assertRaises(CloudError) as context:
            cloud.exec('info')
        self.assertEqual(CloudError.INVALID_OPERATION.code, context.exception.code)

    def test_get_container_returns_container_object(self):
        cloud = Cloud(CloudType.local, login=False)
        cloud._client = docker_client_mock()
        container = cloud.get_container('test-container')
        cloud._client.containers.get.assert_called_once_with('test-container')
        self.assertIsInstance(container, Container)
        self.assertEqual(container.name, 'test-container')

    def test_get_containers_returns_wrapped_containers(self):
        cloud = Cloud(CloudType.local, login=False)
        cloud._client = docker_client_mock()
        cloud._client.containers.list.return_value = [
            MagicMock(name='first'),
            MagicMock(name='second'),
        ]
        cloud._client.containers.list.return_value[0].name = 'first'
        cloud._client.containers.list.return_value[1].name = 'second'
        containers = cloud.get_containers({'status': 'running'})
        cloud._client.containers.list.assert_called_once_with(filters={'status': 'running'})
        self.assertEqual([container.name for container in containers], ['first', 'second'])

    def test_containers_property_gets_all_containers(self):
        cloud = Cloud(CloudType.dockerhub, login=False)
        cloud._client = docker_client_mock()
        cloud._client.containers.list.return_value = []
        self.assertEqual(cloud.containers, [])
        cloud._client.containers.list.assert_called_once_with(filters=None)

    def test_get_containers_invalid_operation_for_gcloud(self):
        cloud = Cloud(CloudType.gcloud, login=False)
        with self.assertRaises(CloudError) as context:
            cloud.get_containers()
        self.assertEqual(CloudError.INVALID_OPERATION.code, context.exception.code)

    def test_get_image_returns_image_object(self):
        cloud = Cloud(CloudType.local, login=False)
        cloud._client = docker_client_mock()
        cloud._client.images.get.return_value = MagicMock()
        image = cloud.get_image('test:latest')
        self.assertIsInstance(image, Image)
        self.assertEqual(image.name, 'test:latest')


class TestImage(TestCase):
    def setUp(self):
        self.cloud = Cloud(CloudType.local, login=False)
        self.client = docker_client_mock()
        self.cloud._client = self.client

    def test_context_manager_enter_returns_self(self):
        self.client.images.get.return_value = MagicMock()
        image = Image(self.cloud, 'test:latest')
        with image as context:
            self.assertIs(context, image)

    def test_context_manager_exit_returns_false(self):
        self.client.images.get.return_value = MagicMock()
        image = Image(self.cloud, 'test:latest')
        self.assertFalse(image.__exit__(None, None, None))

    def test_image_properties_are_read_only(self):
        self.client.images.get.return_value = MagicMock()
        image = Image(self.cloud, 'test:latest')
        with self.assertRaises(AttributeError):
            image.name = 'other:latest'
        with self.assertRaises(AttributeError):
            image.cloud = MagicMock()

    def test_missing_image_has_no_tags(self):
        self.client.images.get.side_effect = ImageNotFound('missing')
        image = Image(self.cloud, 'missing:latest')
        self.assertIsNone(image._ref)
        self.assertEqual(image.tags, [])

    def test_tags_returns_reference_tags(self):
        reference = MagicMock()
        reference.tags = ['test:latest', 'test:v1']
        self.client.images.get.return_value = reference
        image = Image(self.cloud, 'test:latest')
        self.assertEqual(image.tags, ['test:latest', 'test:v1'])

    def test_pull_updates_reference_and_returns_self(self):
        pulled = MagicMock()
        self.client.images.get.return_value = None
        self.client.images.pull.return_value = pulled
        image = Image(self.cloud, 'test:latest')
        result = image.pull()
        self.client.images.pull.assert_called_once_with('test:latest')
        self.assertIs(result, image)
        self.assertIs(image._ref, pulled)

    def test_push_parses_server_log(self):
        self.client.images.get.return_value = MagicMock()
        self.client.images.push.return_value = '{"status": "done"}\n{"status": "complete"}\n'
        image = Image(self.cloud, 'test:latest')
        result = image.push()
        self.client.images.push.assert_called_once_with('test:latest')
        self.assertEqual(result, [{'status': 'done'}, {'status': 'complete'}])

    def test_push_raises_image_error_for_server_error(self):
        self.client.images.get.return_value = MagicMock()
        self.client.images.push.return_value = '{"error": "push failed"}\n'
        image = Image(self.cloud, 'test:latest')
        with self.assertRaises(CloudError) as context:
            image.push()
        self.assertEqual(CloudError.IMAGE_ERROR.code, context.exception.code)

    def test_run_pulls_and_starts_container(self):
        reference = MagicMock()
        self.client.images.get.return_value = reference
        container = MagicMock()
        self.client.containers.run.return_value = container
        image = Image(self.cloud, 'test:latest')
        self.client.images.pull.return_value = reference
        result = image.run(detach=False, environment={'MODE': 'test'})
        self.client.images.pull.assert_called_once_with('test:latest')
        self.client.containers.run.assert_called_once_with('test:latest', detach=False, environment={'MODE': 'test'})
        self.assertIs(result, container)

    def test_run_without_update_does_not_pull(self):
        self.client.images.get.return_value = MagicMock()
        image = Image(self.cloud, 'test:latest')
        image.run(update=False)
        self.client.images.pull.assert_not_called()

    def test_run_invalid_operation_for_gcloud(self):
        cloud = Cloud(CloudType.gcloud, login=False)
        cloud._client = docker_client_mock()
        cloud._client.images.get.return_value = MagicMock()
        image = Image(cloud, 'test:latest')
        with self.assertRaises(CloudError) as context:
            image.run(update=False)
        self.assertEqual(CloudError.INVALID_OPERATION.code, context.exception.code)

    def test_tag_pulls_tags_and_pushes_new_image(self):
        reference = MagicMock()
        self.client.images.get.return_value = reference
        self.client.images.pull.return_value = reference
        self.client.images.push.return_value = '{"status": "done"}\n'
        image = Image(self.cloud, 'test:latest')
        result = image.tag('test:v1')
        reference.tag.assert_called_once_with('test:v1')
        self.assertIsInstance(result, Image)
        self.assertEqual(result.name, 'test:v1')
        self.client.images.push.assert_called_once_with('test:v1')

    def test_tag_missing_reference_raises_image_error(self):
        self.client.images.get.side_effect = ImageNotFound('missing')
        image = Image(self.cloud, 'missing:latest')
        with patch.object(image, 'pull'):
            with self.assertRaises(CloudError) as context:
                image.tag('missing:v1')
        self.assertEqual(CloudError.IMAGE_ERROR.code, context.exception.code)

    def test_dockerhub_image_checks_registry_status(self):
        cloud = Cloud(CloudType.dockerhub, auth=('user', 'password'), login=False)
        cloud._client = docker_client_mock()
        cloud._client.images.get.side_effect = ImageNotFound('missing')
        response = MagicMock(status_code=404)
        with patch('batcave.cloudmgr.get_head', return_value=response) as mock_head:
            image = Image(cloud, 'namespace/test:latest')
        mock_head.assert_called_once_with(
            'https://registry.hub.docker.com/v2/namespace/test/manifests/latest',
            auth=('user', 'password'),
            headers={'Accept': 'application/vnd.docker.distribution.manifest.v2+json'},
            timeout=10,
        )
        self.assertIsNone(image._ref)


class TestContainer(TestCase):
    def setUp(self):
        self.cloud = Cloud(CloudType.local, login=False)
        self.client = docker_client_mock()
        self.cloud._client = self.client

    def test_context_manager_enter_returns_self(self):
        self.client.containers.get.return_value = MagicMock()
        container = Container(self.cloud, 'test-container')
        with container as context:
            self.assertIs(context, container)

    def test_context_manager_exit_returns_false(self):
        self.client.containers.get.return_value = MagicMock()
        container = Container(self.cloud, 'test-container')
        self.assertFalse(container.__exit__(None, None, None))

    def test_properties_are_read_only(self):
        self.client.containers.get.return_value = MagicMock()
        container = Container(self.cloud, 'test-container')
        with self.assertRaises(AttributeError):
            container.name = 'other'
        with self.assertRaises(AttributeError):
            container.cloud = MagicMock()

    def test_stop_forwards_to_docker_reference(self):
        stopped = MagicMock()
        reference = MagicMock()
        reference.stop.return_value = stopped
        self.client.containers.get.return_value = reference
        container = Container(self.cloud, 'test-container')
        result = container.stop()
        reference.stop.assert_called_once_with()
        self.assertIs(result, stopped)

    def test_gcloud_container_is_invalid_operation(self):
        cloud = Cloud(CloudType.gcloud, login=False)
        with self.assertRaises(CloudError) as context:
            Container(cloud, 'test-container')
        self.assertEqual(CloudError.INVALID_OPERATION.code, context.exception.code)

    def test_stop_invalid_operation_for_gcloud(self):
        cloud = Cloud(CloudType.gcloud, login=False)
        cloud._client = docker_client_mock()
        container = object.__new__(Container)
        container._cloud = cloud
        container._name = 'test-container'
        container._ref = MagicMock()
        with self.assertRaises(CloudError) as context:
            container.stop()
        self.assertEqual(CloudError.INVALID_OPERATION.code, context.exception.code)


if __name__ == '__main__':
    main()

# cSpell:ignore dockerhub syscmd cloudmgr
