from rest_framework import serializers
from streetanimal.models import Animal, Category


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
