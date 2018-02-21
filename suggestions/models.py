from django.db import models
from datetime import datetime

class Suggestion(models.Model):
    suggestion_title = models.CharField(max_length=50)
    suggestion_text = models.TextField()
    votes = models.IntegerField(default=0)
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.suggestion_title


class Comment(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    comment_text = models.TextField()
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.comment_text
