import shutil
import tempfile
import unittest

import lesana
from lesana import types


class DerivedType(types.LesanaString):
    """
    A custom type
    """
    name = 'derived'


class Derivative(lesana.Collection):
    """
    A class serived from lesana.Collection
    """


class testDerivatives(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        shutil.copytree(
            'tests/data/derivative',
            self.tmpdir.name,
            dirs_exist_ok=True
        )
        self.collection = Derivative(self.tmpdir.name)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_load_subclasses(self):
        self.assertIsInstance(self.collection.fields['unknown'], DerivedType)


if __name__ == '__main__':
    unittest.main()
