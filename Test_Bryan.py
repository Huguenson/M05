import unittest
def sum(iterable):
    """Return the sum of a list of numbers."""
    total = 0
    for num in iterable:
        total += num
    return total

class TestSum(unittest.TestCase):
    def test_sum_list(self):
        """Test that it can sum a list of integers."""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == "__main__":
    unittest.main()

