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
    monthly_income = models.IntegerField()
    residential_type = models.CharField(max_length=10, choices=[
        ("Apartment", "Apartment"),
        ("Villa", "Villa"),
        ("Housing", "Housing"),
        ("Oneroom", "Oneroom"),
        ("Officetel", "Officetel"),
    ], blank=False)
    have_pet_or_not = models.BooleanField()
    picture_of_residence1 = models.ImageField()
    picture_of_residence2 = models.ImageField()
    picture_of_residence3 = models.ImageField()
    status = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

