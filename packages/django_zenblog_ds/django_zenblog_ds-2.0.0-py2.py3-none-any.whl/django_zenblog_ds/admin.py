from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Post, Profile
from mdeditor.widgets import MDEditorWidget


class PostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(Post, PostModelAdmin)
admin.site.register(Profile)
