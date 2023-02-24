from django.db import models

class websitee(models.Model):
    pname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.IntegerField()
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)
    pin=models.IntegerField()
    address=models.CharField(max_length=50)
    year=models.IntegerField()
    role=models.CharField(max_length=50)
    date=models.DateField()
    class meta:
        db_table="dusers"
    