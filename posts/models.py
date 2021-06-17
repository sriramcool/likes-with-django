from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null = True)
    caption = models.TextField()
    post_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    liked_on = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_id','post_id'],  name="unique_blog_likes")
        ]

    def __str__(self):
        return f'{self.user_id.username} --> {self.post_id.title}' 
