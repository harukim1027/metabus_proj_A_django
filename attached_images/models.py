from django.db import models
from accounts.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(TimestampedModel):
    image_no = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)