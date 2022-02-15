from rest_framework import serializers
from adopt_assignment.models import AdoptAssignment


class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"
        depth = 2

