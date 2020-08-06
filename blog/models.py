from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    description = models.CharField(blank=True, null=True ,max_length=300)
    date_posted = models.DateTimeField(default = timezone.now, blank=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)  
    def __str__(self):
        return str(self.id) + " " + self.title +  " " + self.author.username
    def unique(self):
        return "a" + str(self.id)
    def get_absolute_url(self):
        return reverse( 'post-detail', kwargs={'pk': self.pk})
#class Comments()