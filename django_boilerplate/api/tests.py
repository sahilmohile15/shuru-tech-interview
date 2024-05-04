from django.test import TestCase

# Create your tests here.
class TestMyHome(TestCase):
    def test_get_view(self):
        response = self.client.get("http://127.0.0.1:8000/api/")
        self.assertEqual(response.status_code, 200)