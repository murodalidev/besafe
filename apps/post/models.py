from django.db import models
from django.db.models.signals import post_save
from apps.accounts.models import Account


class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(upload_to='posts/')
    is_main = models.BooleanField(default=False)


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_children(self):
        children = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.top_level_comment_id)
        return children


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        parent = instance
        while parent.parent_comment:
            parent = parent.parent_comment
        instance.top_level_comment_id = parent.id
        instance.save()
    return instance


post_save.connect(comment_post_save, sender=Comment)
