from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from django.http import JsonResponse

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    liked_posts = []

    if request.user.is_authenticated:
        for liked_post in request.user.likes.all():
            liked_posts.append(liked_post.post_id)

    return render(request, 'home.html', {'posts':posts, 'liked_posts':liked_posts})

@login_required 
def like(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(pk = post_id)
    liked = True

    like_object, created = Like.objects.get_or_create(user_id = request.user, post_id = post)
    if not created:
        like_object.delete() # the user already liked this picture before
        liked = False
    
    return JsonResponse({'liked':liked})
