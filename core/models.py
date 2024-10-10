from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class NoteData(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='notes')

    def __str__(self):
        return self.name
