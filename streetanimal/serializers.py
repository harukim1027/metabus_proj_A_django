from django.contrib.auth import get_user_model
from rest_framework import serializers
from streetanimal.models import Animal


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["admin_id"]


class AnimalSerializer(serializers.ModelSerializer):
    admin_id = AuthorSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = ["animal_no", "sex", "date_of_discovery"]

