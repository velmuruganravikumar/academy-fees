from django.db import models

# Create your models here.

class course(models.Model):
    course_name=models.CharField(max_length=30,null=False,blank=False)
    
    def __str__(self):
        return self.course_name

class type(models.Model):
    types=models.CharField(max_length=20,null=False,blank=False)
    
    def __str__(self):
        return self.types

class student(models.Model):
    stdid=models.CharField(max_length=20,unique=True,null=False,blank=False)
    name=models.CharField(max_length=20,null=False,blank=False)
    college=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    student_type=models.ForeignKey(type,on_delete=models.CASCADE)
    courses=models.ForeignKey(course,on_delete=models.CASCADE)
    fees=models.IntegerField(default=0)
    contact=models.IntegerField()
    email=models.EmailField()
    joindate=models.DateField()
    payment_amount=models.IntegerField(default=0)
    paid=models.IntegerField(default=0)
    slot1=models.IntegerField(default=0)
    slot2=models.IntegerField(default=0)
    slot3=models.IntegerField(default=0)
    slot1date=models.DateField(null=True,blank=True)
    slot2date=models.DateField(null=True,blank=True)
    slot3date=models.DateField(null=True,blank=True)
    pending=models.IntegerField(default=0)