from rest_framework import serializers
<<<<<<< HEAD
=======

from attached_images.models import Images
from attached_images.serializers import ImageSerializer
>>>>>>> 94d4ad8e72f627daeda2202c5ce5ce11584a09af
from notice.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = Notice
        fields = "__all__"
=======
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.noticeimage_set.all()
        return ImageSerializer(instance=image, many=True).data

    class Meta:
        model = Notice
        fields = ['notice_no', 'title', 'content', 'created_at', 'images']

    def create(self, validated_data):
        instance = Notice.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            Images.objects.create(notice=instance, image=image_data)
        return instance
>>>>>>> 94d4ad8e72f627daeda2202c5ce5ce11584a09af

