from django import forms
from .models import Word, Definition

class WordForm(forms.ModelForm):   
    class Meta:
        model = Word
        fields = ['name', ]
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("This string must be a word")
        return name.lower()

DefinitionInlineFormSetAdd = forms.inlineformset_factory(Word, Definition, fields=('description',), can_delete=False)
DefinitionInlineFormSetEdit = forms.inlineformset_factory(Word, Definition, fields=('description',))