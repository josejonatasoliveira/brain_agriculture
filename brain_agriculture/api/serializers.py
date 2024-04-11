from rest_framework import serializers

from .models import Produtor, City, State, PlantedCrops

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()
    class Meta:
        model = City
        fields = '__all__'

class ProdutorRequest(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'

class PlantedCropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedCrops
        fields = '__all__'
        
class ProdutorSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    planted_crops = PlantedCropsSerializer(many=True)
    
    class Meta:
        model = Produtor
        fields = '__all__'

    def create(self, validated_data):
        return Produtor.objects.create(**validated_data)