from rest_framework import serializers

from inquiry_board.models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ["inquiry_no", "title", "content", "admin_answer"]

