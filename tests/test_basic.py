import unittest
import toml
import sdrcap


class TestBasicPackage(unittest.TestCase):
    """Test package setup"""

    def test_pkg_version(self):
        """Check if the pyproject version matches package version"""
        with open("../pyproject.toml", "r") as f:
            pyproject_data = toml.load(f)

        toml_version = pyproject_data["tool"]["poetry"]["version"]
        init_version = sdrcap.__version__

        self.assertEqual(toml_version, init_version)


if __name__ == "__main__":
    unittest.main()
