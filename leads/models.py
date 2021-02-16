from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # put null to all leads when agent is deleted
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# signals


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    # if user is created, create user-profile
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
