import unittest
import sdrcap

class TestBasicPackage(unittest.TestCase):

    def test_pkg_version(self):
        self.assertEqual(sdrcap.__version__, "0.0.1")


if __name__ == '__main__':
    unittest.main()