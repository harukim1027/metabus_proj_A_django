from rest_framework import serializers
from adopt_assignment.models import AdoptAssignment


class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AdoptAssignment
        fields = "__all__"
        depth = 2

