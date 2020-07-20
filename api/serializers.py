from rest_framework import serializers
from .models import Linkman

class LinkmanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Linkman
        fields = ['name', 'sex', 'tel', 'email', 'created_at', 'updated_at']

