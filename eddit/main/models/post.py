from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True, editable=False)
    author = models.ForeignKey(User)
    post_title = models.TextField(max_length=50)
    post_date = models.DateTimeField(auto_now=True)
    post_link = models.TextField()
