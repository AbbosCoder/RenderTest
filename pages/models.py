from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title= models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.title)
