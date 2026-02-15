"""Unit tests for the sysutil module."""

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name
# flake8: noqa

from enum import Enum
from multiprocessing import Process, Queue
from os import fdopen, getenv
from pathlib import Path
from stat import S_IRGRP, S_IROTH, S_IRUSR
from sys import platform
from tempfile import mkdtemp, mkstemp
from unittest import main, TestCase

from batcave.sysutil import (chmod, CMDError, get_app_config_dir, get_app_data_dir,
                             LockError, LockFile, LockMode, OSUtilError,
                             popd, pushd, rmpath, rmtree_hard, syscmd, SysCmdRunner)

LockSignal = Enum('LockSignal', ('true', 'false'))


class TestAppDirs(TestCase):
    APP_NAME = 'TestBatCaveApp'

    def test_data_dir_return_type(self):
        self.assertIsInstance(get_app_data_dir(self.APP_NAME), Path)

    def test_config_dir_return_type(self):
        self.assertIsInstance(get_app_config_dir(self.APP_NAME), Path)

    def test_data_dir_app_name(self):
        self.assertEqual(get_app_data_dir(self.APP_NAME).name, self.APP_NAME)

    def test_config_dir_app_name(self):
        self.assertEqual(get_app_config_dir(self.APP_NAME).name, self.APP_NAME)

    def test_data_dir_platform_path(self):
        match platform:
            case 'win32':
                expected = Path(getenv('LOCALAPPDATA', '')) / self.APP_NAME
            case 'darwin':
                expected = Path.home() / 'Library/Application Support' / self.APP_NAME
            case _:
                expected = Path(getenv('XDG_DATA_HOME', Path.home() / '.local/share')) / self.APP_NAME
        self.assertEqual(get_app_data_dir(self.APP_NAME), expected)

    def test_config_dir_platform_path(self):
        match platform:
            case 'win32':
                expected = Path(getenv('APPDATA', '')) / self.APP_NAME
            case 'darwin':
                expected = Path.home() / 'Library/Preferences' / self.APP_NAME
            case _:
                expected = Path(getenv('XDG_CONFIG_HOME', Path.home() / '.config')) / self.APP_NAME
        self.assertEqual(get_app_config_dir(self.APP_NAME), expected)


class TestChmod(TestCase):
    def test_chmod_directory(self):
        tempdir = Path(mkdtemp())
        try:
            chmod(tempdir, S_IRUSR | S_IRGRP | S_IROTH)
            mode = tempdir.stat().st_mode
            match platform:
                case 'win32':
                    pass  # Windows chmod is limited
                case _:
                    self.assertTrue(mode & S_IRUSR)
        finally:
            tempdir.chmod(0o700)
            tempdir.rmdir()

    def test_chmod_recursive(self):
        tempdir = Path(mkdtemp())
        subdir = tempdir / 'sub'
        subdir.mkdir()
        testfile = subdir / 'file.txt'
        testfile.write_text('test')
        try:
            chmod(tempdir, 0o755, recursive=True)
            match platform:
                case 'win32':
                    pass  # Windows chmod is limited
                case _:
                    self.assertTrue(subdir.stat().st_mode & S_IRUSR)
                    self.assertTrue(testfile.stat().st_mode & S_IRUSR)
        finally:
            rmtree_hard(tempdir)

    def test_chmod_files_only(self):
        tempdir = Path(mkdtemp())
        testfile = tempdir / 'file.txt'
        testfile.write_text('test')
        try:
            original_dir_mode = tempdir.stat().st_mode
            chmod(tempdir, 0o644, recursive=True, files_only=True)
            self.assertEqual(tempdir.stat().st_mode, original_dir_mode)
        finally:
            rmtree_hard(tempdir)


class TestDirStack(TestCase):
    def setUp(self):
        self._tempdir = Path(mkdtemp()).resolve()

    def tearDown(self):
        self._tempdir.rmdir()

    def test_popd_empty_stack(self):
        self.assertEqual(popd(), 0)

    def test_push_and_pop(self):
        start = Path.cwd()

        old_dir = pushd(self._tempdir)
        new_dir = Path.cwd()
        self.assertEqual(old_dir, start)
        self.assertEqual(new_dir, self._tempdir)

        old_dir = popd()
        new_dir = Path.cwd()
        self.assertEqual(old_dir, start)
        self.assertEqual(new_dir, start)


class TestExceptions(TestCase):
    def test_PlatformException(self):
        try:
            raise CMDError(CMDError.INVALID_OPERATION, platform='bad-platform')
        except CMDError as err:
            self.assertEqual(CMDError.INVALID_OPERATION.code, err.code)


class TestLockFile(TestCase):
    def setUp(self):
        (fd, fn) = mkstemp()
        self._fh = fdopen(fd)
        self._fn = Path(fn)
        self._got_lock = Queue()
        self._lock_again = Process(target=secondary_lock_process, args=(self._fn, self._got_lock))

    def tearDown(self):
        self._got_lock.close()
        self._fh.close()
        if self._fn.exists():
            self._fn.unlink()

    def test_1_cleanup(self):
        with LockFile(self._fn, handle=self._fh, cleanup=True):
            pass
        self.assertFalse(self._fn.exists())

    def test_2_no_cleanup(self):
        with LockFile(self._fn, handle=self._fh, cleanup=False):
            pass
        self.assertTrue(self._fn.exists())

    def test_3_lock(self):
        with LockFile(self._fn, handle=self._fh, cleanup=True):
            self._lock_again.start()
            got_lock = self._got_lock.get()
            self._lock_again.join()
            self.assertTrue(got_lock == LockSignal.false)

    def test_4_unlock(self):
        with LockFile(self._fn, handle=self._fh, cleanup=True) as lockfile:
            lockfile.action(LockMode.unlock)
            self._lock_again.start()
            got_lock = self._got_lock.get()
            self._lock_again.join()
            lockfile.action(LockMode.lock)
            self.assertTrue(got_lock == LockSignal.true)


def secondary_lock_process(filename, queue):
    try:
        with LockFile(filename, cleanup=False) as lock_again:
            lock_again.action(LockMode.unlock)
            queue.put(LockSignal.true)
    except LockError:
        queue.put(LockSignal.false)


class TestOSUtilError(TestCase):
    def test_group_exists(self):
        try:
            raise OSUtilError(OSUtilError.GROUP_EXISTS, group='test_group')
        except OSUtilError as err:
            self.assertEqual(OSUtilError.GROUP_EXISTS.code, err.code)

    def test_invalid_operation(self):
        try:
            raise OSUtilError(OSUtilError.INVALID_OPERATION, platform='bad-platform')
        except OSUtilError as err:
            self.assertEqual(OSUtilError.INVALID_OPERATION.code, err.code)

    def test_user_exists(self):
        try:
            raise OSUtilError(OSUtilError.USER_EXISTS, user='testuser')
        except OSUtilError as err:
            self.assertEqual(OSUtilError.USER_EXISTS.code, err.code)


class TestRmPath(TestCase):
    def test_remove_file(self):
        (fd, fn) = mkstemp()
        fdopen(fd).close()
        path = Path(fn)
        self.assertTrue(path.exists())
        rmpath(path)
        self.assertFalse(path.exists())

    def test_remove_directory(self):
        tempdir = Path(mkdtemp())
        self.assertTrue(tempdir.exists())
        rmpath(tempdir)
        self.assertFalse(tempdir.exists())

    def test_remove_directory_with_contents(self):
        tempdir = Path(mkdtemp())
        (tempdir / 'subdir').mkdir()
        (tempdir / 'subdir' / 'file.txt').write_text('test')
        (tempdir / 'file.txt').write_text('test')
        rmpath(tempdir)
        self.assertFalse(tempdir.exists())


class TestRmtreeHard(TestCase):
    def test_remove_tree(self):
        tempdir = Path(mkdtemp())
        (tempdir / 'subdir').mkdir()
        (tempdir / 'subdir' / 'file.txt').write_text('test')
        rmtree_hard(tempdir)
        self.assertFalse(tempdir.exists())

    def test_remove_readonly_tree(self):
        tempdir = Path(mkdtemp())
        readonly_file = tempdir / 'readonly.txt'
        readonly_file.write_text('test')
        readonly_file.chmod(S_IRUSR | S_IRGRP | S_IROTH)
        rmtree_hard(tempdir)
        self.assertFalse(tempdir.exists())


class TestSysCmd(TestCase):
    def test_basic_command(self):
        match platform:
            case 'win32':
                result = syscmd('cmd', '/c', 'echo', 'hello')
            case _:
                result = syscmd('echo', 'hello')
        self.assertTrue(any('hello' in line for line in result))

    def test_flatten_output(self):
        match platform:
            case 'win32':
                result = syscmd('cmd', '/c', 'echo', 'hello', flatten_output=True)
            case _:
                result = syscmd('echo', 'hello', flatten_output=True)
        self.assertIsInstance(result, str)
        self.assertIn('hello', result)

    def test_cmd_not_found(self):
        with self.assertRaises((CMDError, FileNotFoundError)):
            syscmd('this_command_does_not_exist_batcave')

    def test_remote_options_without_remote(self):
        with self.assertRaises(CMDError) as context:
            syscmd('echo', 'hello', remote_auth=('user', 'pass'))
        self.assertEqual(CMDError.INVALID_OPERATION.code, context.exception.code)


class TestSysCmdRunner(TestCase):
    def test_basic_run(self):
        match platform:
            case 'win32':
                runner = SysCmdRunner('cmd', '/c', 'echo', show_cmd=False, show_stdout=False)
                result = runner.run('hello')
            case _:
                runner = SysCmdRunner('echo', show_cmd=False, show_stdout=False)
                result = runner.run('hello')
        self.assertTrue(any('hello' in line for line in result))


if __name__ == '__main__':
    main()

# cSpell:ignore batcave localappdata syscmd
