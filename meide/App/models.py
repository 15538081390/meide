from django.db import models

# Create your models here.
class Index(models.Manager):
    sid = models.AutoField(primary_key=True)
    pid = models.AutoField(null=True)
