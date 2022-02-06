from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Animal(TimestampedModel):
    animal_no = models.AutoField(primary_key=True)
    size = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_discovery = models.DateTimeField()
    place_of_discovery = models.DateTimeField()
    physical_condition = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    protection_status = models.CharField(max_length=30)
    image = models.ImageField()
