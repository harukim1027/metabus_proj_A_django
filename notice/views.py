<<<<<<< HEAD
from rest_framework import viewsets
from notice.models import Notice
from notice.serializers import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
=======
from django.shortcuts import render
from rest_framework import viewsets

from notice.models import Notice
from notice.serializers import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

>>>>>>> 94d4ad8e72f627daeda2202c5ce5ce11584a09af
