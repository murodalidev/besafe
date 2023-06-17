from django.db import models
from apps.accounts.models import Account


def file_path(instance, filename):
    return f"{instance.message.room_id}/{filename}"


class Chat(models.Model):
    TYPE = (
        (0, 'private'),
        (1, 'group'),
    )
    members = models.ManyToManyField(Account, related_name='chats')
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(choices=TYPE, default=0)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def messages_count(self):
        return self.messages.count()

    def __str__(self):
        return str(self.id)


class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_members', on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, related_name='messages')
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='senders')
    message = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Media(models.Model):
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, related_name='medias')
    file = models.FileField(upload_to=file_path)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

