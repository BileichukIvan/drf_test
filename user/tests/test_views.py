from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User, Team


class UserViewSetTest(APITestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Engineering")
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "teams": [self.team.id]
        }
        self.user = User.objects.create(**self.user_data)

    def make_request(self, method, url, data=None):
        """Helper method to make requests."""
        return getattr(self.client, method)(url, data, format="json")

    def test_create_user(self):
        """Test creating a new user"""
        response = self.make_request("post", "/users/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_list_users(self):
        """Test listing users"""
        response = self.make_request("get", "/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user(self):
        """Test retrieving a user by ID"""
        response = self.make_request("get", f"/users/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user(self):
        """Test updating a user`s information"""
        updated_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "teams": [self.team.id]
        }
        response = self.make_request("put", f"/users/{self.user.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Jane")

    def test_delete_user(self):
        """Test deleting a user"""
        response = self.make_request("delete", f"/users/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
