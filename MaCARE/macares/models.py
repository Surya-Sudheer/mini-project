from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age=models.IntegerField(default='10')
    yesno=models.CharField(max_length=3)
    district=models.CharField(max_length=50)
    wardno=models.IntegerField()
    phone=models.IntegerField()
    cmp = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    ashaid = models.IntegerField(default='0')
    lastmen = models.DateField(settings.DATE_FORMAT,default="2002-02-01")
    lastpg = models.DateField(settings.DATE_FORMAT,default="2002-02-01")
    bg = models.CharField(max_length=20,default="A+")
    rchid=models.IntegerField(default='0')

    def __str__(self):
        return self.email
    
class Month(models.Model):
    uid=models.IntegerField()
    mid= models.AutoField(primary_key=True)
    data_dict = {
        'did' : '0',
        'title' : 'awesome title',
        'body' : 'great body of text',
    }
    
# class atri(models.Model):
#     uid=models.IntegerField()
#     month = models.ForeignKey(Month)
    