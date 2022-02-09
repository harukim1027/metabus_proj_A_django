from rest_framework.viewsets import ModelViewSet
from streetanimal.models import Animal
from streetanimal.serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
