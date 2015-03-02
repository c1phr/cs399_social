from django.db import models
from main.models.user import User


class Post(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    author = models.ForeignKey(User)
    post_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
