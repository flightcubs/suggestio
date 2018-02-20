from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Suggestion, Comment

class IndexView(generic.ListView):
    template_name = 'suggestions/index.html'
    context_object_name = 'latest_suggestion_list'

    def get_queryset(self):
        """Return the last published suggestions."""
        return Suggestion.objects.order_by('-submit_date')[:10]


class DetailView(generic.DetailView):
    model = Suggestion
    template_name = 'suggestions/detail.html'
