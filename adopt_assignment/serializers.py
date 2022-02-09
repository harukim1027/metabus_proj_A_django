from django.contrib.auth import get_user_model
from rest_framework import serializers
from adopt_assignment.models import AdoptAssignment
from streetanimal.serializers import AnimalSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["userID", "nickname"]


class AssignmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    animal = AnimalSerializer(read_only=True)

    class Meta:
        model = AdoptAssignment
        fields = "__all__"

