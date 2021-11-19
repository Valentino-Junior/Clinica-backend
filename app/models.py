from django.db import models
import datetime as dt
from django.urls import reverse
from url_or_relative_url_field.fields import URLOrRelativeURLField

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{ self.name }"

class Vaccine(models.Model):
    vaccine = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255, null=True)
    batch_number = models.DecimalField(max_digits=12, decimal_places=2)
    drug_expiry = models.DateField()
    user_profile = CloudinaryField('image')
    next_appointment=models.CharField(max_length=50)
    date_given = models.DateField()
    

    def __str__(self):
        return f"{ self.vaccine }"




# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image')
    contact = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"CartID : { self.pk }"

    def get_absolute_url(self):
        return reverse('vaccine_detail', kwargs={'pk': self.pk})
    
          
    
    # growth=======>
class Growth(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    HO = models.IntegerField()
    date = models.DateField()
    

    def __str__(self):
        return f"{ self.patient.username }"
    
    def get_absolute_url(self):
            return reverse('', kwargs={'pk': self.pk})


# emerging disease==============>
class EmergingDisease(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=200)
    next_appointment=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{ self.disease_name }"

    def get_absolute_url(self):
        return reverse('desease_detail', kwargs={'pk': self.pk})

   
    
    
    