from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    #one to one relationship b/n profile image
    # and user 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()
    def __str__(self):
        return f'{self.user.username} Profile'

