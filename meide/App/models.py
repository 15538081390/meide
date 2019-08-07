from django.db import models

# Create your models here.
class Index(models.Manager):
<<<<<<< HEAD
    sid = models.AutoField(primary_key=True)
    pid = models.IntegerField(null=True)
    name =models.CharField(max_length=11)
=======
    sabbid = models.AutoField(primary_key=True)
    pid = models.AutoField(null=True)
   
    def niubi():
        print('哈哈哈，贼牛逼')
>>>>>>> 768023f54f8c5f78fb4f9d5ef888eebd109c3106
