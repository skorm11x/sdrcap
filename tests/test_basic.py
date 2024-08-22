import unittest
import sdrcap

class TestBasicPackage(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_pkg_version(self):
        """_summary_
        """
        self.assertEqual(sdrcap.__version__, "0.0.1")


if __name__ == '__main__':
    unittest.main()