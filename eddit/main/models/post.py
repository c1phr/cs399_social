from django.db import models
from main.models import user


class Post(models.Model):
    author = models.ForeignKey(user)
    post_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()