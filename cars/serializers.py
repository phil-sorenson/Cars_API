from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price']   # If one of the fields was taken out, the outside world would never be able to see it (E.g 'make'). Data/field still exists in DB but no where else
        
