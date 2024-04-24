from django.test import TestCase
from .models import CustomUser

class CustomUserTests(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')
