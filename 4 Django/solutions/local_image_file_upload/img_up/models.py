from django.db import models

class ImageDocument(models.Model):
    image_file = models.ImageField()