from django import forms
from .models import Word, Definition

class WordForm(forms.ModelForm):   
    class Meta:
        model = Word
        fields = ['name', ]

DefinitionInlineFormSetAdd = forms.inlineformset_factory(Word, Definition, fields=('description',), can_delete=False)
DefinitionInlineFormSetEdit = forms.inlineformset_factory(Word, Definition, fields=('description',))