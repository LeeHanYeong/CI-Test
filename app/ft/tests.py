from django.test import TestCase


class SampleTest(TestCase):
    def test_fail(self):
        self.assertEqual(2, 1)
