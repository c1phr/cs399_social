import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models.comment import Comment
from main.models.post import Post


@login_required
def posts(request):
    post_id = request.GET.get('id', None)
    if not post_id:
        return render(request, "main/posts.html", {'posts': Post.objects.all()})
    return render(request, "main/post_detail.html", {'post': Post.objects.filter(id=post_id).first(), 'comments': Comment.objects.filter(parent_post=post_id)})

@login_required
def post_comment(request):
    if request.method == 'POST':
        comment = Comment()
        comment.author = request.user
        comment.parent_post = Post.objects.filter(id=request.POST.get("post-id", "")).first()
        comment.comment_content = request.POST.get("comment-text", "")
        comment.save()
        return HttpResponseRedirect("/posts/?id=" + request.POST.get("post-id", ""))
    else:
        return posts(request)