from django.db import models
from accounts.models import User
from adopt_assignment.models import AdoptAssignment
from adopt_review.models import Review
from notice.models import Notice


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(TimestampedModel):
    image_no = models.AutoField(primary_key=True)
    image1 = models.ImageField(upload_to='', blank=True)
    image2 = models.ImageField(upload_to='', blank=True)
    image3 = models.ImageField(upload_to='', blank=True)
    image4 = models.ImageField(upload_to='', blank=True)
    image5 = models.ImageField(upload_to='', blank=True)
    category = models.CharField(max_length=30, blank=True)
    notice_no = models.ForeignKey(Notice, on_delete=models.CASCADE, blank=True)
    review_no = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True)
    assignment_no = models.ForeignKey(AdoptAssignment, on_delete=models.CASCADE, blank=True)

