from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    hospital=models.CharField(max_length=50)
    age=models.IntegerField()
    yesno=models.CharField(max_length=3)
    district=models.CharField(max_length=50)
    wardno=models.IntegerField()
    phone=models.IntegerField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20,)
    password = models.CharField(max_length=20)
    cmp = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    
