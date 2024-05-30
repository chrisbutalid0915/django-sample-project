from rest_framework import serializers
from .models import Location

class LocationBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude']

    def validate_latitude(self, value):
        """Check that latitude is within the valid range."""
        if not -90 <= value <= 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90 degrees.")
        return value
    

    def validate_longitude(self, value):
        """Check that longitude is within the valid range."""
        if not -180 <= value <= 180:
            raise serializers.ValidationError("Longitude must be between -180 and 90 degreses.")
        return value
    

    def validate(self, data):
        """Custom validation for latitude and longitude together"""
        if data['latitude'] == 0 and data['longitude'] == 0:
            raise serializers.ValidationError("Invalid location: both latitude and longitude cannot be zero.")
        return data

class LocationCreateSerializer(LocationBaseSerializer):
    pass


class LocationUpdateSerializer(LocationBaseSerializer):
    pass