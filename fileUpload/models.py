from django.db import models

# Create your models here.

# file uploading- imagefiled (need pillow pkg) / filefield 

class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to="images")
    bio = models.TextField()

    def __str__(self):
        return self.name
    # pip install pillow
