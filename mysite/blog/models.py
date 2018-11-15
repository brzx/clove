from django.db import models
from myauth import models as authmodel

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(authmodel.User, on_delete=models.CASCADE)
    created = models.DateTimeField('date created')
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=2000)

    def __str__(self):
        return self.title