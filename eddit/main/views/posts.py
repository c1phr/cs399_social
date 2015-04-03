import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from main.models.comment import Comment
from main.models.post import Post


@login_required
def posts(request):
    post_id = request.GET.get('id', None)
    if not post_id:
        return render(request, "main/posts.html")
    return render(request, "main/post_detail.html", {'post': Post.objects.filter(id=post_id).first(), 'comments': Comment.objects.filter(parent_post=post_id)})

@login_required
def posts_partial(request):
    return render(request, "main/_post_list.html", {'posts': Post.objects.all()})

@login_required
def upvote(request):
    if request.method == 'POST':
        post_id = request.POST.get("post_id")
        post = Post.objects.filter(id=post_id).first()
        post.post_votes += 1
        post.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

def downvote(request):
    if request.method == 'POST':
        post_id = request.POST.get("post_id")
        post = Post.objects.filter(id=post_id).first()
        post.post_votes -= 1
        post.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

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