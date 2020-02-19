from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Pet


class PetSerializer(ModelSerializer):
    view_count = serializers.ReadOnlyField()
    version_number = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    def get_version_number(self, obj):
        return '3'
