import datetime
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super().save(*args, **kwargs)

    def check_password_hash(self, password):
        if check_password(password, self.password):
            return True
        else:
            return False