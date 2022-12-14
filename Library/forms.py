from django import forms


class SearchForm(forms.Form):
    choiceList = (
        ('category', 'Category'),
        ('name', 'Name of book'),
        ('author', 'Author')
    )
    search = forms.CharField(max_length=30)
    filter = forms.ChoiceField(choices=choiceList)
