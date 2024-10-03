from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSetTestCase(APITestCase):
    def setUp(self):
        """Create some test data"""
        self.team1 = Team.objects.create(name="Development Team")
        self.team2 = Team.objects.create(name="QA Team")

        self.list_url = reverse('team-list')  # Assuming you're using routers for the viewset
        self.detail_url = lambda pk: reverse('team-detail', kwargs={'pk': pk})

    def create_team(self, name):
        return self.client.post(self.list_url, {"name": name}, format='json')

    def test_list_teams(self):
        """Test list view (GET /teams/)"""
        response = self.client.get(self.list_url)
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_team(self):
        """Test retrieve view (GET /teams/{id}/)"""
        response = self.client.get(self.detail_url(self.team1.id))
        serializer = TeamSerializer(self.team1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_team(self):
        """Test create view (POST /teams/)"""
        response = self.create_team("New Team")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 3)

    def test_update_team(self):
        """Test update view (PUT /teams/{id}/)"""
        response = self.client.put(self.detail_url(self.team1.id), {"name": "Updated Team"}, format='json')
        self.team1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.team1.name, "Updated Team")

    def test_delete_team(self):
        """Test delete view (DELETE /teams/{id}/)"""
        response = self.client.delete(self.detail_url(self.team2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 1)
