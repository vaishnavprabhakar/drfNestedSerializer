from django.contrib import admin
from . models import (Author,
                      Poll
                    )
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'created_at', 'updated_at']
