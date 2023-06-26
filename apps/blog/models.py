from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    title = models.CharField(max_length=221, verbose_name=_('Category'))

    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    description = RichTextField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(upload_to='blogs/')
    is_main = models.BooleanField(default=False)


