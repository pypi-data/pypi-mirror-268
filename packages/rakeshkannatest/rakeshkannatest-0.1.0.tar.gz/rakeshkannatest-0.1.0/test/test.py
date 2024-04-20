
import unittest
from rakeshkannatest import hello 

# Define a test class
class TestHelloFunction(unittest.TestCase):

    # Define a test method to test hello() function
    def test_hello(self):
        # Call the hello() function
        result = hello()

        # Assert the result
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()

