from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from streetanimal.models import Animal
from streetanimal.serializers import AnimalSerializer, AnimalCreateSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AnimalSerializer
        return AnimalCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal_reg_num__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]

