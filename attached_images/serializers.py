from rest_framework import serializers
from attached_images.models import Images


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Images
        fields = ["image"]

