from django.conf import settings
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notice(TimestampedModel):
    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()


    