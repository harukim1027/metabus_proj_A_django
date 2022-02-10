from rest_framework import serializers
from adopt_assignment.models import AdoptAssignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"

