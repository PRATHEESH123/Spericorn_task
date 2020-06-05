from rest_framework import serializers

# local
from ..models import Members


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('id', 'team','name','category','date_of_birth','contact_detail')