from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import date

from .models import Suggestion, Comment
from .forms import SuggestionForm, CommentForm

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
        return Suggestion.objects.order_by('-votes')

class DetailView(generic.DetailView):
    model = Suggestion
    template_name = 'suggestions/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the comments for the current suggestion
        context['comments'] = Comment.objects.filter(suggestion = self.kwargs['pk'])
        # Add the comment form
        context['form'] = CommentForm
        return context

def vote(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    suggestion.votes += 1
    suggestion.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('suggestions:detail', args=(suggestion.id,)))

def new_suggestion(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SuggestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            new_suggestion = Suggestion(suggestion_title = title, suggestion_text = text)
            new_suggestion.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('suggestions:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SuggestionForm()

    return render(request, 'suggestions/new.html', {'form': form})


def comment(request, suggestion_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            text = form.cleaned_data['text']
            suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
            new_comment = Comment(suggestion = suggestion, comment_text = text)
            new_comment.save()

            # redirect back to suggestion:
            return HttpResponseRedirect(reverse('suggestions:detail', args=(suggestion.id,)))

    # if a GET (or any other method) we'll redirect back to suggestion
    else:
        return HttpResponseRedirect(reverse('suggestions:detail', args=(suggestion.id,)))

def resetExample(request):
    Suggestion.objects.all().delete()
    s01 = Suggestion(suggestion_title = "Buy a new coffee brewer to the office", suggestion_text = "Seriously, we need to talk about this. I think we could increase productivity by at least 35 percent by buying a new coffee brewer. In addition, the employees would be happier. Coffee is important, y'all. ", votes = 47, submit_date = date(2017,12,29))
    s02 = Suggestion(suggestion_title = "Have a conference in Italy", suggestion_text = "We should go to Italy and eat pasta. Nothing brings a team together like pasta!", votes = 1, submit_date = date(2018,1,22))
    s03 = Suggestion(suggestion_title = "Get standing desks", suggestion_text = "You know what they say, sitting kills. We should get standing desks so we can work standing up. Please vote for #standingdesks2018!", votes = 18, submit_date = date(2018,2,7))
    s01.save()
    s02.save()
    s03.save()
    c01 = Comment(suggestion_id = s01.id, comment_text = "Yes - I'd love this too!")
    c02 = Comment(suggestion_id = s01.id, comment_text = "This would be awesome <3")
    c03 = Comment(suggestion_id = s03.id, comment_text = "I'm not sure about this one...")
    c01.save()
    c02.save()
    c03.save()
    return HttpResponseRedirect(reverse('suggestions:index'))
