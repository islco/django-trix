from django.contrib import admin
from .models import Post

from trix.admin import TrixAdmin


@admin.register(Post)
class PostAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('content',)
