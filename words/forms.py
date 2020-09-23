from django import forms
from .models import Word, Definition

class WordForm(forms.ModelForm):   
    class Meta:
        model = Word
        fields = ['name', ]

DefinitionInlineFormSet = forms.inlineformset_factory(Word, Definition, fields=('description',))