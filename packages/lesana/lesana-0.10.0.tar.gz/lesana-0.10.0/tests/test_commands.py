import contextlib
import io
import os
import shutil
import tempfile
import unittest

import hazwaz.unittest

from lesana import command


class Args:
    def __init__(self, args):
        self.args = args

    def __getattribute__(self, k):
        try:
            return super().__getattribute__(k)
        except AttributeError:
            try:
                return self.args[k]
            except KeyError as e:
                raise AttributeError(e)


class CommandsMixin:
    def _edit_file(self, filepath):
        return True

    def _run_command(self, cmd, args):
        stream = {
            'stdout': io.StringIO(),
            'stderr': io.StringIO(),
        }
        cmd.edit_file_in_external_editor = self._edit_file
        cmd.args = Args(args)
        with contextlib.redirect_stdout(stream['stdout']):
            with contextlib.redirect_stderr(stream['stderr']):
                cmd.main()
        return stream


class testCommandsSimple(hazwaz.unittest.HazwazTestCase, CommandsMixin):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/simple',
            self.tmpdir.name,
            dirs_exist_ok=True,
        )
        self.lesana = command.Lesana()
        for cmd in self.lesana.commands:
            cmd.editors = [("true", "true")]
        # re-index the collection before running each test
        self.run_with_argv(self.lesana, [
            "lesana",
            "index",
            "-c", self.tmpdir.name,
            "--reset"
        ])

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_init(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "init",
            "-c", self.tmpdir.name,
        ])
        self.assertEqual(streams['stdout'].getvalue(), '')
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_new(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "new",
            "-c", self.tmpdir.name,
        ])
        self.assertEqual(len(streams['stdout'].getvalue()), 33)
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_edit(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "edit",
            "-c", self.tmpdir.name,
            "11189ee4",
        ])
        self.assertTrue("11189ee4" in streams['stdout'].getvalue())
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_show(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "show",
            "-c", self.tmpdir.name,
            "11189ee4"
        ])
        self.assertTrue(
            'name: Another item' in streams['stdout'].getvalue()
        )
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_index(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "index",
            "-c", self.tmpdir.name,
            "--reset",
        ])
        self.assertEqual(
            streams['stdout'].getvalue(),
            'Found and indexed 3 entries\n',
        )
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_search(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "search",
            "-c", self.tmpdir.name,
            "Another"
        ])
        self.assertTrue(
            '11189ee4' in streams['stdout'].getvalue()
        )
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_get_values(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "get-values",
            "-c", self.tmpdir.name,
            "--field", "position",
        ])
        self.assertIn('somewhere: 2', streams['stdout'].getvalue())
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_export(self):
        with tempfile.TemporaryDirectory() as dest_tmpdir:
            shutil.copytree(
                'tests/data/simple',
                dest_tmpdir,
                dirs_exist_ok=True,
            )
            # TODO: make finding the templates less prone to breaking and
            # then remove the cwd change from here
            old_cwd = os.getcwd()
            os.chdir(self.tmpdir.name)
            streams = self.run_with_argv(self.lesana, [
                "lesana",
                "export",
                "-c", self.tmpdir.name,
                "--query", "Another",
                dest_tmpdir,
                "templates/from_self.yaml",
            ])
            os.chdir(old_cwd)
            self.assertEqual(streams['stdout'].getvalue(), '')
            self.assertEqual(streams['stderr'].getvalue(), '')

    def test_remove(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "rm",
            "-c", self.tmpdir.name,
            "11189ee4"
        ])
        self.assertEqual(streams['stdout'].getvalue(), '')
        self.assertEqual(streams['stderr'].getvalue(), '')
        # and check that the entry has been removed
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "show",
            "-c", self.tmpdir.name,
            "11189ee4"
        ])
        self.assertEqual(streams['stderr'].getvalue(), '')
        # TODO: check that the file is no longer there

    def test_update(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "update",
            "-c", self.tmpdir.name,
            "--field", "position",
            "--value", "here",
            "Another"
        ])
        self.assertEqual(streams['stdout'].getvalue(), '')
        self.assertEqual(streams['stderr'].getvalue(), '')


class testCommandsComplex(hazwaz.unittest.HazwazTestCase, CommandsMixin):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/complex',
            self.tmpdir.name,
            dirs_exist_ok=True,
        )
        self.lesana = command.Lesana()
        for cmd in self.lesana.commands:
            cmd.editors = [("true", "true")]
        # re-index the collection before running each test
        self.run_with_argv(self.lesana, [
            "lesana",
            "index",
            "-c", self.tmpdir.name,
            "--reset",
        ])

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_get_values_from_list(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "get-values",
            "-c", self.tmpdir.name,
            "--field", "tags",
        ])
        self.assertIn('this: 1', streams['stdout'].getvalue())
        self.assertEqual(streams['stderr'].getvalue(), '')

    def test_search_template(self):
        streams = self.run_with_argv(self.lesana, [
            "lesana",
            "search",
            "-c", self.tmpdir.name,
            "--expand-query-template",
            "{{ nice }}"
        ])
        self.assertIn('8e9fa1ed', streams['stdout'].getvalue())
        self.assertIn('5084bc6e', streams['stdout'].getvalue())
        self.assertEqual(streams['stderr'].getvalue(), '')


if __name__ == '__main__':
    unittest.main()
