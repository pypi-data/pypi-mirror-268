import unittest
from unittest import TestCase

from tool_use.tools.openai_tool_use import (
    CompletionNoneException,
    CompletionNoneExceptionFlag,
)


class TestCompletionNoneException(TestCase):
    def test_first_exception_function(self):
        """
        Test the is_first_exception function
        - return true, when the exception is raised first time.
        - return false, when the exception is raised more than once.
        """
        flag = CompletionNoneExceptionFlag()
        for i in range(10):
            exception = CompletionNoneException()
            if i == 0:
                self.assertTrue(exception.is_first_exception(flag))
            else:
                self.assertFalse(exception.is_first_exception(flag))

    def test_counter(self):
        """Test the flag value each time when the exception is raised."""
        flag = CompletionNoneExceptionFlag()
        for i in range(10):
            if i == 0:
                self.assertFalse(flag.get_flag())
            else:
                self.assertTrue(flag.get_flag())

            exception = CompletionNoneException()
            exception.is_first_exception(flag)


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
