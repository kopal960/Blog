from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    image = models.ImageField(default= 'default.jpg' , upload_to= 'profile_media')
    def __str__(self):
        return  self.user.username+str(self.image) 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width>300 or img.height >300:
            img.thumbnail((300,300))
        img.save(self.image.path) 