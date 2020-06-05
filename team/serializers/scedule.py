from rest_framework import serializers

# local
from ..models import Scedule


class SceduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scedule
        fields = ('id', 'date','venue','result')