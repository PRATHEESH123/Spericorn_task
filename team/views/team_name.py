from rest_framework import viewsets
from rest_framework import mixins

# local
from ..models import Team_Name
from ..serializers import Team_nameSerializer


class Team_nameViewSet(viewsets.ModelViewSet):
    queryset = Team_Name.objects.all()
    serializer_class = Team_nameSerializer