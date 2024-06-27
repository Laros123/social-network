from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Branch(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('branch-detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk,
                                              'bk': self.branch.pk})

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Commentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commentary = models.ForeignKey('Commentary', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.text}'
    
    class Meta:
        ordering=['-created']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
