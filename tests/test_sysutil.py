"""Unit tests for the sysutil module."""

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name
# flake8: noqa

from enum import Enum
from multiprocessing import Process, Queue
from os import fdopen, getenv
from pathlib import Path
from sys import platform
from tempfile import mkdtemp, mkstemp
from unittest import main, TestCase

from batcave.sysutil import (pushd, popd, CMDError, get_app_config_dir,
                             get_app_data_dir, LockFile, LockError, LockMode)

LockSignal = Enum('LockSignal', ('true', 'false'))


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

    # @skip('Problems with secondary process')
    def test_3_lock(self):
        with LockFile(self._fn, handle=self._fh, cleanup=True):
            self._lock_again.start()
            got_lock = self._got_lock.get()
            self._lock_again.join()
            self.assertTrue(got_lock == LockSignal.false)

    # @skip('Problems with secondary process')
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


class TestDirStack(TestCase):
    def setUp(self):
        self._tempdir = Path(mkdtemp()).resolve()

    def tearDown(self):
        self._tempdir.rmdir()

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
                expected = Path(getenv('LOCALAPPDATA', ''), self.APP_NAME)
            case 'darwin':
                expected = Path.home() / 'Library/Application Support' / self.APP_NAME
            case _:
                expected = Path(getenv('XDG_DATA_HOME', Path.home() / '.local/share'), self.APP_NAME)
        self.assertEqual(get_app_data_dir(self.APP_NAME), expected)

    def test_config_dir_platform_path(self):
        match platform:
            case 'win32':
                expected = Path(getenv('APPDATA', ''), self.APP_NAME)
            case 'darwin':
                expected = Path.home() / 'Library/Preferences' / self.APP_NAME
            case _:
                expected = Path(getenv('XDG_CONFIG_HOME', Path.home() / '.config'), self.APP_NAME)
        self.assertEqual(get_app_config_dir(self.APP_NAME), expected)


if __name__ == '__main__':
    main()

# cSpell:ignore batcave localappdata
