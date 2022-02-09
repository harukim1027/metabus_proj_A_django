from rest_framework import viewsets
from attached_images.models import Images
from attached_images.serializers import ImagesSerializer


class AttachedImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
