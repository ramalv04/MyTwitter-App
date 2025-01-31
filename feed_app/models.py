from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_tweets', blank=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.content

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()