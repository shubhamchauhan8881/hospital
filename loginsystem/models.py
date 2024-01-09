from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone  = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='uploads/patients/profile_pics/', blank=True)
    address =  models.CharField(max_length=255)
    city  = models.CharField(max_length=100 ,null=True, blank=True)
    state = models.CharField(max_length=100 ,null=True, blank=True)
    pincode = models.CharField(max_length=15 ,null=True, blank=True)

    def __str__( self):
        return self.user.first_name


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone  = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='uploads/doctors/profile_pics/', blank=True)
    address =  models.CharField(max_length=255)
    doctor_id = models.CharField(max_length=100)
    doctor_qualifications = models.CharField(max_length=500)
    city  = models.CharField(max_length=100 , null=True,blank=True )
    state = models.CharField(max_length=100 , null=True,blank=True)
    pincode = models.CharField(max_length=15 , null=True,blank=True )

    def __str__( self):
        return self.user.first_name
