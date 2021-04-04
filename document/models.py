from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
