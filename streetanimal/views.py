from rest_framework.viewsets import ModelViewSet
from streetanimal.models import Animal
from streetanimal.serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal_reg_num__icontains=query)

        return qs
