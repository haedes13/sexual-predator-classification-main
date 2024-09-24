from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from forums.sexual_checker import check_message

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    @property
    def get_post_category(self):
        if hasattr(self, 'postcategory'):
            return PostCategory.objects.filter(post=self).first()
        else:
            return check_message(self.content)

    class Meta:
        ordering = ['-date_posted']
    
class PostCategory(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category.capitalize()


