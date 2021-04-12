from rest_framework import serializers
from .models import Peak

class PeakListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = [
            'id',
            'name',
            'lat',
            'lon',
            'alt'
        ]