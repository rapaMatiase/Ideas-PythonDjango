from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    detail = models.CharField(max_length=300, default="Sin detalle")
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return "{}".format(self.id)

class ImagePostModel(models.Model):
    
    image = models.ImageField()
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)