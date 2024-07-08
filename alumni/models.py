from django.db import models

class Alumni(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    grad_year = models.IntegerField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='alumni_images/')


