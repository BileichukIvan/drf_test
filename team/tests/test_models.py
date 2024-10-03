from django.test import TestCase

from team.models import Team


class TeamModelTest(TestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Development")

    def test_team_creation(self):
        """Test if a team is created successfully."""
        self.assertEqual(self.team.name, "Development")
        self.assertTrue(isinstance(self.team, Team))
        self.assertEqual(str(self.team), "Development")

    def test_unique_team_name(self):
        """Test that a team with a duplicate name cannot be created."""
        with self.assertRaises(Exception):
            Team.objects.create(name="Development")

    def test_team_str_representation(self):
        """Test the string representation of the team."""
        team = Team(name="Design")
        self.assertEqual(str(team), "Design")
