from django.conf import settings
from django.db import models

from accounts.models import User
from streetanimal.models import Animal


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdoptAssignment(TimestampedModel):
    assignment_no = models.AutoField(primary_key=True)
    adopter_name = models.CharField(max_length=30, db_index=True)
    monthly_income = models.IntegerField()
    residential_type = models.CharField(max_length=10, choices=[
        ("Apartment", "Apartment"),
        ("Villa", "Villa"),
        ("Housing", "Housing"),
        ("Oneroom", "Oneroom"),
        ("Officetel", "Officetel"),
    ], default="Apartment")
    have_pet_or_not = models.BooleanField()
    picture_of_residence1 = models.ImageField()
    picture_of_residence2 = models.ImageField()
    picture_of_residence3 = models.ImageField()
    status = models.CharField(max_length=3, choices=(
        ("1", "신청"),
        ("2", "심사 중"),
        ("3", "수락"),
        ("4", "교육 중"),
        ("5", "입양 완료"),
        ("6", "거절"),
    ), default=1, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, unique=True)

