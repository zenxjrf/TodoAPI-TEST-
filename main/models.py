from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=20)
    time = models.TimeField()
    description = models.TextField()
    status = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)