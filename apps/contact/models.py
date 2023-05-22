from django.db import models
from apps.accounts.models import Account


class Relationship(models.Model):
    title = models.CharField(max_length=221)
    is_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=221)
    name = models.CharField(max_length=221)
    phone = models.CharField(max_length=12)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
