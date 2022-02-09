from rest_framework import serializers
from streetanimal.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["animal_no", "sex", "age", "date_of_discovery"]

