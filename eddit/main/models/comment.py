from django.contrib.auth.models import User
from django.db import models
from main.models.post import Post


class Comment(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True, editable=False)
    author = models.ForeignKey(User)
    parent_post = models.ForeignKey(Post)
    comment_date = models.DateTimeField(auto_now=True)
    comment_content = models.TextField()
