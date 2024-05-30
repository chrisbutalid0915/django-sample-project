from rest_framework import serializers
from .models import Address

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'location', 'latitude', 'longitude']