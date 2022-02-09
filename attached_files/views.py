from rest_framework import viewsets
from attached_files.serializers import AttachedFileSerializer
from attached_files.models import AttachedFile


class AttachedFileViewSet(viewsets.ModelViewSet):
    queryset = AttachedFile.objects.all()
    serializer_class = AttachedFileSerializer
