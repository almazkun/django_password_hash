from django.test import TestCase, Client
from django.urls import reverse
from hashhash.models import CustomUser

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {"email": "my_email@email.com", "password": "my_password"}

    def test_model_s(self):
        response = self.client.post(reverse("model_s"), self.user_data)
        user = CustomUser.objects.get(email=self.user_data["email"])

        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_serializer(self):
        response = self.client.post(reverse("serializer"), self.user_data)
        user = CustomUser.objects.get(email=self.user_data["email"])

        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))
