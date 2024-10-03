from django.test import TestCase
from user.models import User, Team


class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Engineering")
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        self.user.teams.add(self.team)

    def test_user_creation(self):
        """Test if a team is created successfully."""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.teams.count(), 1)

    def test_user_str_representation(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), "John Doe")
