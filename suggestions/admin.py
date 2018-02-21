from django.contrib import admin

from .models import Suggestion, Comment

# Register the models for admin page
admin.site.register(Suggestion)
admin.site.register(Comment)
