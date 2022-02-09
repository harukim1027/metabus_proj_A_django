from rest_framework import viewsets
from inquiry_board.serializers import InquirySerializer
from inquiry_board.models import Inquiry


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
