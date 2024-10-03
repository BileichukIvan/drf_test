from rest_framework import serializers

from team.models import Team
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "teams"]
