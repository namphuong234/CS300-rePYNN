from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)