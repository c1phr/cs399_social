from rest_framework import serializers
from main.models.comment import Comment
from main.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment