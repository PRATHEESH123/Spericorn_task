from rest_framework import serializers

# local
from ..models import Team_Name


class Team_nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team_Name
        fields = ('id', 'name','score')