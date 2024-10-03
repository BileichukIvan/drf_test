from rest_framework.test import APITestCase
from user.models import User, Team
from user.serializers import UserSerializer


class UserSerializerTest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Engineering")
        self.user = self._create_user_with_team(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            teams=[self.team.id]
        )

    @staticmethod
    def _create_user_with_team(first_name, last_name, email, teams):
        """Helper method to create a user with teams"""
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.teams.add(*teams)
        return user

    def test_user_serializer_valid_data(self):
        """Test serializer with valid data"""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "teams": [self.team.id]
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data["first_name"], user_data["first_name"]
        )
        self.assertEqual(
            serializer.validated_data["teams"][0].id, self.team.id
        )

    def test_user_serializer_invalid_data(self):
        """Test serializer with invalid email data"""
        invalid_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid_email",
            "teams": [self.team.id]
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
