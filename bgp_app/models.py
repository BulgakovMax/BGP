from django.db import models


# Create your models here.
class Topic(models.Model):
    """Topic, which explorer user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
