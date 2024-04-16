import decimal
import unittest

from lesana import templating


class testFilters(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_to_yaml(self):
        res = templating.to_yaml(None)
        self.assertIsInstance(res, str)
        self.assertEqual(res, 'null')

        s = "A short string"
        res = templating.to_yaml(s)
        self.assertEqual(res, s)

        s = """
        A long, multiline
        string
        with multiple
        lines
        """
        res = templating.to_yaml(s)
        self.assertIsInstance(res, str)
        self.assertTrue(res.startswith('|'))
        self.assertIn('\n', res)

        s = """
        short
        multiline
        """
        res = templating.to_yaml(s)
        self.assertIsInstance(res, str)
        self.assertTrue(res.startswith('|'))
        self.assertIn('\n', res)

        res = templating.to_yaml(10)
        self.assertEqual(res, '10')

        res = templating.to_yaml(decimal.Decimal('10.1'))
        self.assertEqual(res, "'10.1'")

        s = "A very long line, but one that has no new lines " \
            + "even if it is definitely longer than a standard " \
            + "80 columns line"
        res = templating.to_yaml(s)
        self.assertTrue(res.startswith("|\n"))
        self.assertNotIn('\n', res.lstrip("|\n"))
        for line in res.lstrip("|\n").split('\n'):
            self.assertTrue(line.startswith("  "))


if __name__ == '__main__':
    unittest.main()
