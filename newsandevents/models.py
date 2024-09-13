from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(upload_to='news_images/')
    date = models.DateField()
    
    def __str__(self):
        return self.title   
    
class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(upload_to='event_images/')
    date = models.DateField()
    
    def __str__(self):
        return self.title