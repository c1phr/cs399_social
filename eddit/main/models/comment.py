from django.db import models
from main.models.post import Post
#from main.models.user import User


class Comment(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True, editable=False)
    #author = models.ForeignKey(User)
    parent_post = models.ForeignKey(Post)
    comment_date = models.DateTimeField(auto_now=True)
    comment_content = models.TextField()
