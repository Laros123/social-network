from django.db import models
from django.conf import settings

# Create your models here.


class Branch(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='posts')
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Commentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments')
    commentary = models.ForeignKey('Commentary', on_delete=models.DO_NOTHING, related_name='comment', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.text}'
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
