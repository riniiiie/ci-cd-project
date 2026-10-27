import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
