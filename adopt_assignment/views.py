from rest_framework import viewsets

from adopt_assignment.models import AdoptAssignment
from adopt_assignment.serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(assignment_no__icontains=query) or qs.filter(adopter_name__icontains=query)

        return qs

