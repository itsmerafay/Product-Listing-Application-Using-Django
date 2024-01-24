from django.db import models
from django.contrib.auth.models import User # it's a built in user model provided by django


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="receipe", null=True, blank=True)