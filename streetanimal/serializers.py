from rest_framework import serializers
from streetanimal.models import Animal


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        field = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1

