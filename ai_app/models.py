from django.db import models

class ImageElement(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="mediaphoto", blank=True, null=True)
