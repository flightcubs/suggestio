from django.template import loader
from django.shortcuts import render
from django.http import Http404

from .models import Suggestion, Comment

def index(request):
    latest_suggestion_list = Suggestion.objects.order_by('-submit_date')[:5]
    context = {'latest_suggestion_list': latest_suggestion_list}
    return render(request, 'suggestions/index.html', context)

def detail(request, suggestion_id):
    try:
        suggestion = Suggestion.objects.get(pk=suggestion_id)
    except Suggestion.DoesNotExist:
        raise Http404("Suggestion does not exist")
    comments = Comment.objects.filter(suggestion = suggestion_id)
    return render(request, 'suggestions/detail.html', {'suggestion': suggestion, 'comments':comments})
