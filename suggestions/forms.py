from django import forms

class SuggestionForm(forms.Form):
    title = forms.CharField(label='Suggestion title', max_length=50)
    text = forms.CharField(widget=forms.Textarea)
