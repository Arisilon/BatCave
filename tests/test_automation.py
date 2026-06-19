"""Unit tests for the automation module."""

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name,protected-access
# flake8: noqa

from io import StringIO
from logging import getLogger
from pathlib import Path
from typing import Callable
from unittest import main, TestCase
from unittest.mock import MagicMock, call, patch

from batcave.automation import Action, ActionCommandRunner
from batcave.sysutil import SysCmdRunner


class ConcreteAction(Action):
    """Concrete implementation of abstract Action for testing."""

    def __init__(self, execute_fn: Callable | None = None, **kwargs):
        """Initialize ConcreteAction with optional execute function.

        Args:
            execute_fn (optional): Callable to execute in _execute().
            **kwargs: Passed to parent Action.

        Attributes:
            execute_fn: The function to call during _execute.
            pre_called: Track if pre() was called.
            post_called: Track if post() was called.
            always_post_called: Track if always_post() was called.
        """
        super().__init__(**kwargs)
        self.execute_fn = execute_fn or (lambda: None)
        self.pre_called = False
        self.post_called = False
        self.always_post_called = False

    def _execute(self) -> None:
        self.execute_fn()

    def pre(self) -> None:
        self.pre_called = True

    def post(self) -> None:
        self.post_called = True

    def always_post(self) -> None:
        self.always_post_called = True
        super().always_post()


class TestActionCommandRunnerInitialization(TestCase):  # pylint: disable=protected-access
    """Test ActionCommandRunner initialization and attribute setup."""

    def test_logger_default_is_print(self):
        runner = ActionCommandRunner('echo')
        self.assertEqual(runner.logger, print)

    def test_logger_callable_stored_directly(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger)
        self.assertEqual(runner.logger, mock_logger)

    def test_logger_instance_uses_info_method(self):
        logger_instance = getLogger('test')
        runner = ActionCommandRunner('echo', logger=logger_instance)
        self.assertEqual(runner.logger, logger_instance.info)

    def test_guard_default_empty_string(self):
        runner = ActionCommandRunner('echo')
        self.assertEqual(runner.guard, '')

    def test_guard_stored_correctly(self):
        runner = ActionCommandRunner('echo', guard='Building...')
        self.assertEqual(runner.guard, 'Building...')

    def test_none_logger_stored_correctly(self):
        runner = ActionCommandRunner('echo', logger=None)
        self.assertIsNone(runner.logger)

    def test_command_passed_to_parent(self):  # pylint: disable=protected-access
        runner = ActionCommandRunner('echo')
        self.assertEqual(runner._command, 'echo')

    def test_syscmd_args_passed_to_parent(self):  # pylint: disable=protected-access
        syscmd_args = {'use_shell': True}
        runner = ActionCommandRunner('echo', syscmd_args=syscmd_args)
        self.assertIn('use_shell', runner._default_syscmd_args)  # pylint: disable=protected-access
        self.assertEqual(runner._default_syscmd_args['use_shell'], True)  # pylint: disable=protected-access


class TestActionCommandRunnerRun(TestCase):
    """Test ActionCommandRunner.run() method behavior."""

    def test_run_logs_message_with_default_logger(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger)

        with patch.object(SysCmdRunner, 'run', return_value='output'):
            runner.run('Test message')
            mock_logger.assert_called_once_with('Test message')

    def test_run_logs_guard_before_message(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger, guard='Guard line')

        with patch.object(SysCmdRunner, 'run', return_value='output'):
            runner.run('Test message')
            calls = mock_logger.call_args_list
            self.assertEqual(calls[0], call('Guard line'))
            self.assertEqual(calls[1], call('Test message'))

    def test_run_omits_logging_when_logger_none(self):
        runner = ActionCommandRunner('echo', logger=None)

        with patch.object(SysCmdRunner, 'run', return_value='output') as mock_run:
            runner.run('Test message')
            mock_run.assert_called_once()
            # Logger shouldn't be called at all

    def test_run_omits_logging_with_empty_message(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger)

        with patch.object(SysCmdRunner, 'run', return_value='output'):
            runner.run('')
            mock_logger.assert_not_called()

    def test_run_omits_logging_with_none_message(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger)

        with patch.object(SysCmdRunner, 'run', return_value='output'):
            runner.run(None)
            mock_logger.assert_not_called()

    def test_run_forwards_args_to_parent(self):
        runner = ActionCommandRunner('echo')

        with patch.object(SysCmdRunner, 'run', return_value='output') as mock_run:
            runner.run('message', 'arg1', 'arg2')
            mock_run.assert_called_once_with('arg1', 'arg2',
                                             post_option_args=None,
                                             syscmd_args=None)

    def test_run_forwards_post_option_args(self):
        runner = ActionCommandRunner('echo')
        post_args = {'flag': 'value'}

        with patch.object(SysCmdRunner, 'run', return_value='output') as mock_run:
            runner.run('message', post_option_args=post_args)
            mock_run.assert_called_once_with(post_option_args=post_args,
                                             syscmd_args=None)

    def test_run_forwards_syscmd_args(self):
        runner = ActionCommandRunner('echo')
        syscmd_args = {'use_shell': True}

        with patch.object(SysCmdRunner, 'run', return_value='output') as mock_run:
            runner.run('message', syscmd_args=syscmd_args)
            mock_run.assert_called_once_with(post_option_args=None,
                                             syscmd_args=syscmd_args)

    def test_run_returns_parent_result(self):
        runner = ActionCommandRunner('echo')

        with patch.object(SysCmdRunner, 'run', return_value='parent_output'):
            result = runner.run('message')
            self.assertEqual(result, 'parent_output')

    def test_run_with_guard_empty_string_no_logging(self):
        mock_logger = MagicMock()
        runner = ActionCommandRunner('echo', logger=mock_logger, guard='')

        with patch.object(SysCmdRunner, 'run', return_value='output'):
            runner.run('Test message')
            # Guard shouldn't be logged because it's empty
            mock_logger.assert_called_once_with('Test message')


class TestActionInitialization(TestCase):
    """Test Action initialization and properties."""

    def test_action_has_abstractmethod_execute(self):
        # Action.execute is abstract but not via ABC, so instantiation is possible
        # but calling execute without implementing _execute will fail
        action = ConcreteAction()
        self.assertIsInstance(action, Action)

    def test_concrete_action_instantiates(self):
        action = ConcreteAction()
        self.assertIsInstance(action, Action)

    def test_project_root_is_parent_of_cwd(self):
        action = ConcreteAction()
        expected = Path.cwd().parent
        self.assertEqual(action.project_root, expected)

    def test_project_root_is_read_only_property(self):
        action = ConcreteAction()
        with self.assertRaises(AttributeError):
            action.project_root = Path('/tmp')

    def test_message_guard_is_70_asterisks(self):
        self.assertEqual(len(Action.message_guard), 70)
        self.assertTrue(all(c == '*' for c in Action.message_guard))


class TestActionContextManager(TestCase):
    """Test Action context manager protocol."""

    def test_context_manager_enter_returns_self(self):
        action = ConcreteAction()
        with action as ctx:
            self.assertIs(ctx, action)

    def test_context_manager_exit_returns_false(self):
        action = ConcreteAction()
        result = action.__exit__(None, None, None)
        self.assertFalse(result)

    def test_context_manager_exit_with_exception_returns_false(self):
        action = ConcreteAction()
        exc = ValueError('test error')
        result = action.__exit__(type(exc), exc, None)
        self.assertFalse(result)


class TestActionLifecycle(TestCase):
    """Test Action execution lifecycle and method ordering."""

    def test_execute_calls_methods_in_order(self):
        action = ConcreteAction()
        call_order = []

        def track_execute():
            call_order.append('_execute')

        action.execute_fn = track_execute
        original_pre = action.pre
        original_post = action.post
        original_always_post = action.always_post

        def pre():
            call_order.append('pre')
            original_pre()

        def post():
            call_order.append('post')
            original_post()

        def always_post():
            call_order.append('always_post')
            original_always_post()

        action.pre = pre
        action.post = post
        action.always_post = always_post

        with patch('batcave.automation.popd'):
            action.execute()

        self.assertEqual(call_order, ['pre', '_execute', 'post', 'always_post'])

    def test_always_post_called_on_execute_success(self):
        action = ConcreteAction()

        with patch('batcave.automation.popd') as mock_popd:
            action.execute()
            self.assertTrue(action.always_post_called)
            mock_popd.assert_called_once()

    def test_always_post_called_on_execute_exception(self):
        def failing_execute():
            raise ValueError('Test error')

        action = ConcreteAction(execute_fn=failing_execute)

        with patch('batcave.automation.popd') as mock_popd:
            with self.assertRaises(ValueError):
                action.execute()
            self.assertTrue(action.always_post_called)
            mock_popd.assert_called_once()

    def test_exception_from_execute_propagates(self):
        def failing_execute():
            raise RuntimeError('Execution failed')

        action = ConcreteAction(execute_fn=failing_execute)

        with patch('batcave.automation.popd'):
            with self.assertRaises(RuntimeError) as ctx:
                action.execute()
            self.assertEqual(str(ctx.exception), 'Execution failed')

    def test_exception_from_pre_prevents_execute(self):
        def failing_pre():
            raise RuntimeError('Pre failed')

        action = ConcreteAction()
        action.pre = failing_pre
        action.execute_fn = MagicMock()

        with patch('batcave.automation.popd'):
            with self.assertRaises(RuntimeError):
                action.execute()
            action.execute_fn.assert_not_called()

    def test_exception_from_pre_still_calls_always_post(self):
        def failing_pre():
            raise RuntimeError('Pre failed')

        action = ConcreteAction()
        action.pre = failing_pre

        with patch('batcave.automation.popd') as mock_popd:
            with self.assertRaises(RuntimeError):
                action.execute()
            self.assertTrue(action.always_post_called)
            mock_popd.assert_called_once()

    def test_exception_from_post_propagates_after_always_post(self):
        def failing_post():
            raise RuntimeError('Post failed')

        action = ConcreteAction()
        action.post = failing_post

        with patch('batcave.automation.popd') as mock_popd:
            with self.assertRaises(RuntimeError):
                action.execute()
            self.assertTrue(action.always_post_called)
            mock_popd.assert_called_once()


class TestActionLogMessage(TestCase):
    """Test Action.log_message() output formatting."""

    def test_log_message_prints_message_with_default_leader(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message')

        output = captured_output.getvalue()
        self.assertIn('INFO Test message', output)

    def test_log_message_with_guard_true_prints_guard_first(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', guard=True)

        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 2)
        self.assertIn('*' * 70, lines[0])
        self.assertIn('Test message', lines[1])

    def test_log_message_with_guard_false_omits_guard(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', guard=False)

        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 1)
        self.assertNotIn('*' * 70, output)

    def test_log_message_with_empty_leader(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', leader='')

        output = captured_output.getvalue()
        self.assertEqual(output.strip(), 'Test message')
        self.assertNotIn('INFO', output)

    def test_log_message_with_custom_leader(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', leader='ERROR')

        output = captured_output.getvalue()
        self.assertIn('ERROR Test message', output)

    def test_log_message_with_guard_and_custom_leader(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', guard=True, leader='DEBUG')

        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        self.assertIn('DEBUG', lines[0])
        self.assertIn('*' * 70, lines[0])
        self.assertIn('DEBUG Test message', lines[1])

    def test_log_message_flushes_stdout(self):
        action = ConcreteAction()
        mock_stdout = MagicMock()

        with patch('sys.stdout', mock_stdout):
            action.log_message('Test message')

        # sys.stdout.flush() should be called
        mock_stdout.flush.assert_called_once()

    def test_log_message_with_leader_false(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', leader=False)

        output = captured_output.getvalue()
        self.assertEqual(output.strip(), 'Test message')

    def test_log_message_with_leader_zero(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Test message', leader=0)

        output = captured_output.getvalue()
        self.assertEqual(output.strip(), 'Test message')

    def test_log_message_multiline_message(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Line 1\nLine 2')

        output = captured_output.getvalue()
        self.assertIn('INFO Line 1', output)
        self.assertIn('Line 2', output)


class TestActionIntegration(TestCase):
    """Integration tests for Action with custom subclass implementations."""

    def test_custom_action_subclass_full_lifecycle(self):
        execution_log = []

        def custom_execute():
            execution_log.append('execute')

        action = ConcreteAction(execute_fn=custom_execute)

        with patch('batcave.automation.popd'):
            action.execute()

        self.assertTrue(action.pre_called)
        self.assertIn('execute', execution_log)
        self.assertTrue(action.post_called)
        self.assertTrue(action.always_post_called)

    def test_context_manager_with_exception_handling(self):
        def failing_execute():
            raise RuntimeError('Action failed')

        action = ConcreteAction(execute_fn=failing_execute)

        with patch('batcave.automation.popd'):
            try:
                with action:
                    action.execute()
                self.fail('Exception should have been raised')
            except RuntimeError:
                pass  # Expected

        self.assertTrue(action.always_post_called)

    def test_log_message_sequence(self):
        action = ConcreteAction()
        captured_output = StringIO()

        with patch('sys.stdout', captured_output):
            action.log_message('Starting', leader='INFO')
            action.log_message('Progress', leader='INFO')
            action.log_message('Complete', leader='INFO')

        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 3)
        self.assertTrue(all('INFO' in line for line in lines))


if __name__ == '__main__':
    main()

# cSpell:ignore syscmd
