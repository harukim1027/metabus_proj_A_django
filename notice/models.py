from django.conf import settings
from django.db import models

from accounts.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notice(TimestampedModel):
    notice_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

