from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import Post ,Vote
from .models import Profile

@receiver(post_save , sender=User)
def create_profile_and_vote(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(user = instance)
        instance.profile.save()
        for post in Post.objects.all():
            vote = Vote.objects.create(user = instance ,post=post)
            vote.save()
@receiver(post_save ,sender=Post)
def create_vote(sender , instance,created ,**kwargs):
    if created:
        for user in User.objects.all():
            vote = Vote.objects.create(post=instance , user = user)
            vote.save()
