from django.db import models

# Create your models here.
class HomeModel(models.Model):
    bannerText = models.TextField()
    bannerImg = models.ImageField(default='basic.png',blank=True)