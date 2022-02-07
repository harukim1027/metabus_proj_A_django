from django.db import models
from notice.models import Notice


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AttachedFile(TimestampedModel):
    notice_no = models.ForeignKey(Notice, on_delete=models.CASCADE)
    att_file_no = models.IntegerField(max_length=100, db_index=True, blank=False)
    att_file = models.TextField(blank=False)
