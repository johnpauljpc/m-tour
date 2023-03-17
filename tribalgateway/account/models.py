from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from PIL import Image

# Create your models here.
class Usermodel(AbstractUser):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length=100)
    phone_number =models.CharField(max_length=20)
    passport = models.ImageField(default='images/profile.jpeg', upload_to="images/users_passport")
    email = models.EmailField(unique=True)
    nationality =  CountryField(multiple = False)
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)





    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        super(Usermodel, self).save(*args, **kwargs)
        if self.passport:
            img = Image.open(self.passport.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.passport.path)
