from rest_framework import viewsets
from rest_framework import mixins

# local
from ..models import Members
from ..serializers import MembersSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer