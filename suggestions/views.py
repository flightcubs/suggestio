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

def vote(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    suggestion.votes += 1
    suggestion.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('suggestions:detail', args=(suggestion.id,)))
