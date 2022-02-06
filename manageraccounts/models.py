from django.db import models


class ManagerAcc(models.Model):
    admin_id = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=40)

