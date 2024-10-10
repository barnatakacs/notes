from django.contrib import admin
from .models import NoteData, Tag

# Register your models here.

admin.site.register(NoteData)
admin.site.register(Tag)
