from django.db import models
from django.contrib.auth.models import User
import os

class File(models.Model):
    file = models.FileField(upload_to='files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Eliminar el archivo del sistema de archivos
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        
        super().delete(*args, **kwargs)

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    content_type = models.CharField(max_length=10, choices=[
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('video', 'Video')
    ])
    content = models.FileField(upload_to='news_content/', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Distributor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    country1 = models.CharField(max_length=250)
    address = models.TextField()
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
