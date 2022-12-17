from django import forms

from .models import Tags


class SearchForm(forms.Form):
    choiceList = (
        ('category', 'Category'),
        ('name', 'Name of book'),
        ('author', 'Author')
    )
    search = forms.CharField(max_length=200)
    filter = forms.ChoiceField(choices=choiceList)


class AddForm(forms.Form):
    name_of_book = forms.CharField(max_length=200)
    file = forms.FileField(widget=forms.ClearableFileInput)
    tags = forms.CharField(widget=forms.Textarea)
