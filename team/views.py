from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
