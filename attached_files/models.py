from django.db import models
from notice.models import Notice


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AttachedFile(TimestampedModel):
    att_file_no = models.AutoField(primary_key=True)
    notice_no = models.ForeignKey(Notice, on_delete=models.CASCADE)
    att_file = models.TextField(blank=False)
