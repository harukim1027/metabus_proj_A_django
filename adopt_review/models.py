from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from accounts.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(TimestampedModel):
    number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    content = models.TextField()
    image = models.ImageField(blank=True)
