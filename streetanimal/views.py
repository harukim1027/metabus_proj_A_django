from rest_framework import viewsets
from streetanimal.models import Animal, Category
from streetanimal.serializers import AnimalSerializer, CategorySerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal_reg_num__icontains=query)

        return qs


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
