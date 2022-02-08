from rest_framework import serializers
from accounts.models import User
from attached_images.models import Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image_no"]

