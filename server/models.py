from django.conf import settings
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    # Relation is one to many (one server can have many users), So foreign key is in the many side
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="server_owner"
    )

    # Many to many relation (one server can have many categories and one category can have many servers)
    categories = models.ManyToManyField(Category, related_name="categories")

    # Many to many relation (one server can have many members and one member can have many servers)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="server_members")

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    topic = models.CharField(max_length=150, null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="channel_owner"
    )

    # one to many relation (one server can have many channels)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")

    def __str__(self):
        return self.name

    # lower case the name before saving
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="message_sender"
    )
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="message_channel")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} - {self.content}"
