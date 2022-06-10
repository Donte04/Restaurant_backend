# describe the process of going from Python object to JSON

from rest_framework import serializers
from .models import Plat

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = ['id', 'nom', 'ingredients']
