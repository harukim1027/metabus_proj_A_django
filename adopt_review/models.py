from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from accounts.models import User
from adopt_assignment.models import AdoptAssignment


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(TimestampedModel):
    review_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    content = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adoptassignment = models.ForeignKey(AdoptAssignment, on_delete=models.CASCADE, default=(AdoptAssignment.assignment_no if AdoptAssignment.user == user else 1))
    # 해결 안된 adoptassignment


