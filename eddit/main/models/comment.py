from django.db import models
from main.models import user
from main.models.post import Post


class Comment(models.Model):
    author = models.ForeignKey(User)
    parent_post = models.ForeignKey(Post)
    comment_date = models.DateTimeField(auto_now=True)
    comment_content = models.TextField()