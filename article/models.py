from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False)
    content = models.TextField(blank=False, null=False)