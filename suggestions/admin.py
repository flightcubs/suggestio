from django.contrib import admin

from .models import Suggestion, Comment

admin.site.register(Suggestion)
admin.site.register(Comment)
