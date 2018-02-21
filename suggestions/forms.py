from django import forms

class SuggestionForm(forms.Form):
    title = forms.CharField(label='Suggestion title', max_length=50)
    text = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    # Hidden id input for sending Suggestion foreign key
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    text = forms.CharField(label='Write a comment', widget=forms.Textarea)
