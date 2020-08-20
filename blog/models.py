from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

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
        return reverse( 'post-detail', kwargs={'pk': self.pk })
class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    name = models.ForeignKey(User , on_delete=models.CASCADE)
    dated = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    active = models.BooleanField(default = True)
    def __str__(self):
        return self.comment
class Vote(models.Model):
    Like = models.BooleanField(default = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete =models.CASCADE)
    class Meta:
        unique_together = ('user' , 'post')