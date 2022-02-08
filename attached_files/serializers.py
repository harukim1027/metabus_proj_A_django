from rest_framework import serializers
from accounts.models import User
from attached_files.models import AttachedFile


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname"]


class AttachedFileSerializer(serializers.ModelSerializer):
    nickname = AuthorSerializer(read_only=True)

    class Meta:
        model = AttachedFile
        fields = ["notice_no", "att_file_no", "att_file"]

