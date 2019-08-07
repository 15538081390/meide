from django.db import models

# Create your models here.
class Index(models.Manager):

    sid = models.AutoField(primary_key=True)
    pid = models.IntegerField(null=True)
    name =models.CharField(max_length=11)

    def niubi(self):
        print('哈哈哈，贼牛逼')
