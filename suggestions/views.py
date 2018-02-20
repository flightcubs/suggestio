from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Suggestion, Comment



class IndexView(generic.ListView):
    template_name = 'suggestions/index.html'
    context_object_name = 'latest_suggestion_list'
    model = Suggestion

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            # Could pass more things here.
        })
        return context

    def get_queryset(self):
        return Suggestion.objects.order_by('votes')

class DetailView(generic.DetailView):
    model = Suggestion
    template_name = 'suggestions/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the comments for the current suggestion
        context['comments'] = Comment.objects.filter(suggestion = self.kwargs['pk'])
        return context

def vote(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    suggestion.votes += 1
    suggestion.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('suggestions:detail', args=(suggestion.id,)))
