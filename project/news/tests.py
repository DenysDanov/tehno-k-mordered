from django.test import SimpleTestCase, TestCase
from .custom import get_safe_slice as _

class ListTest(SimpleTestCase):
    def test_get_safe_slice(self):
        self.assertEqual(
            [],
            _([],8),
        )
        self.assertEqual(
            [1],
            _([1],8),
        )
        self.assertEqual(
            [1,2,3,4],
            _([1,2,3,4],8),
        )
        self.assertEqual(
            [1,2,3,4,5,6,7,8],
            _([1,2,3,4,5,6,7,8],8),
        )
        self.assertEqual(
            [1,2,3,4,5,6,7,8],
            _([1,2,3,4,5,6,7,8,7,6],8),
        )