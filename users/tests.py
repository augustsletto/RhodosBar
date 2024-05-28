from django.test import TestCase
from .models import User

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            bio='Test bio',
            instagram_link='https://instagram.com/testuser'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.bio, 'Test bio')
        self.assertEqual(self.user.instagram_link, 'https://instagram.com/testuser')
