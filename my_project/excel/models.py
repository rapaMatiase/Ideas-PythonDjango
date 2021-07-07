from django.db import models

# Create your models here.
class MyExcelFiles(models.Model):
    name = models.CharField(max_length=40)
    excel = models.FileField(upload_to='excel/')