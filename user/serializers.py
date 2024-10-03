from rest_framework import serializers
from user.models import User
from team.models import Team


class UserSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "teams"]
