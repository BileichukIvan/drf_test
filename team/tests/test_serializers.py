from django.test import TestCase
from rest_framework.exceptions import ValidationError

from team.models import Team
from team.serializers import TeamSerializer


class TeamSerializerTestCase(TestCase):
    def setUp(self):
        """Create a sample Team instance"""
        self.team = Team.objects.create(name="Development Team")

    def test_team_serialization(self):
        """Test serialization (model -> JSON)"""
        serializer = TeamSerializer(self.team)
        expected_data = {
            "id": self.team.id,
            "name": "Development Team"
        }
        self.assertEqual(serializer.data, expected_data)

    def test_team_deserialization(self):
        """Test deserialization (JSON -> model)"""
        data = {
            "name": "QA Team"
        }
        serializer = TeamSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        team = serializer.save()
        self.assertEqual(team.name, "QA Team")

    def test_team_deserialization_invalid_data(self):
        """Test deserialization with invalid data"""
        data = {
            "name": ""
        }
        serializer = TeamSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.save()
