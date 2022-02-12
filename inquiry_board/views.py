from rest_framework import viewsets
from inquiry_board.serializers import InquirySerializer
from inquiry_board.models import Inquiry


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query) or qs.filter(inquiry_no__icontains=query)

        return qs
