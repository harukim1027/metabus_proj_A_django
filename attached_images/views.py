from django.shortcuts import render
from rest_framework import viewsets

from attached_images.serializers import ImageSerializer
from notice.models import Notice


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = ImageSerializer

