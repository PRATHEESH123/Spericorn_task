from rest_framework import viewsets
from rest_framework import mixins

# local
from ..models import Scedule
from ..serializers import SceduleSerializer


class SceduleViewSet(viewsets.ModelViewSet):
    queryset = Scedule.objects.all()
    serializer_class = SceduleSerializer