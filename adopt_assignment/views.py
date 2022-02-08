from rest_framework import viewsets

from adopt_assignment.models import AdoptAssignment
from adopt_assignment.serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()
    serializer_class = AssignmentSerializer
