from rest_framework import serializers
from attached_files.models import AttachedFile


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"

