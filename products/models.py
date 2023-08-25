from django.db import models
from django.contrib.auth.models import User
import os

class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    file = models.FileField(upload_to='products/')
    file1 = models.FileField(upload_to='products/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    characteristics = models.ManyToManyField(Characteristic)  # Use ManyToManyField for characteristics

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        if self.file1:
            if os.path.isfile(self.file1.path):
                os.remove(self.file1.path)
        super().delete(*args, **kwargs)
