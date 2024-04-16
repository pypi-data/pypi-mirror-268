import unittest

from heiwa4126.hello import Hello, hello


class TestHello(unittest.TestCase):
    """
    A test case for the hello function.
    """

    def test_hello(self):
        """
        Test case for the hello function.
        """
        result = hello()
        expected = "hello"
        self.assertEqual(result, expected)


class TestHelloClass(unittest.TestCase):
    """
    A test case for the hello function.
    """

    def test_hello_class(self):
        """
        Test case for the Hello class.
        """
        h = Hello("hello")
        result = h.say()
        expected = "hello hello"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
