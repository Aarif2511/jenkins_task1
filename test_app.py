import unittest
from app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, Jenkins!_now_1")

if __name__ == "__main__":
    unittest.main()
