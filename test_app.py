from unittest import TestCase
from app import all_users, get_users


class Test(TestCase):
    def test_get_users(self):
        self.assertEqual(len(all_users), len(get_users()))
