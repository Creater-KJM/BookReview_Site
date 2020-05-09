from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=50)
     price = models.IntegerField(default=0)
     evaluate = models.IntegerField(default=0)
     contents = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)

     def __str__(self):
          return self.title