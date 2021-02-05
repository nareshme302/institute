from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Branch(models.Model):
    BRANCH_CHOICES = (('cse', 'CSE'), (' mec', 'MEC'), ('ece', 'ECE'), ('eee', 'EEE'), ('civil', 'CIVIL'))
    branch_name = models.CharField(unique=True, max_length=10, choices=BRANCH_CHOICES)
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.branch_name


class Staff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_created=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_created=True,null=True,blank=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name
