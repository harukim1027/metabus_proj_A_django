from rest_framework import viewsets
from attached_files.serializers import AttachedFileSerializer
from attached_files.models import Attached_file


class AttachedFileViewSet(viewsets.ModelViewSet):
    queryset = Attached_file.objects.all()
    serializer_class = AttachedFileSerializer
