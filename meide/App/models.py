from django.db import models

# Create your models here.
class Index(models.Manager):
    sabbid = models.AutoField(primary_key=True)
    pid = models.AutoField(null=True)
   
    def niubi():
        print('哈哈哈，贼牛逼')
