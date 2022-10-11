from django.db import models

# Create your models here.
class CooperItems(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    item_type = models.CharField(max_length=255)
    item_medium = models.CharField(max_length=255)
    item_image_url = models.CharField(max_length=255)
    item_location = models.CharField(max_length=255)

class VAItems(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    item_type = models.CharField(max_length=255)
    item_medium = models.CharField(max_length=255)
    item_image_url = models.CharField(max_length=255)
    item_location = models.CharField(max_length=255)