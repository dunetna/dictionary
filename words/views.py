from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm, DefinitionInlineFormSet

def index(request):
    context = {}
    # Get partial or complete word to find
    search = request.GET.get('search')
    if search:
        # Get all words starting with string introduced by user
        words = list(Word.objects.filter(name__startswith=search))
        # Send all words to the template
        context.update(words=words)
    return render(request, 'words/index.html', context)

def show(request, word):    
    # Add word and definitions to context to send them to the template
    word = Word.objects.get(name=word)
    context = {'word': word, 'definitions': word.definition_set.all()}
    return render(request, 'words/show.html', context)

def delete(request, word):
    # Remove word and its definitions and go to homepage
    Word.objects.filter(name=word).delete()    
    return redirect('/')

def add_edit(request, word=None):
    # If word is None, action is "add", otherwise is "edit"
    # Create the base object depending on the action to do
    if word is None:
        # Empty object if action is "add"
        word = Word()
    else:
        # Initialized object if action is "edit"
        word = Word.objects.get(name=word)
    if request.method == 'POST':
        # Process sent data        
        if word is None:
            word_form = WordForm(request.POST)
        else:
            word_form = WordForm(request.POST, instance=word)
        if word_form.is_valid():            
            created_word = word_form.save(commit=False)
            # Create an inline formset to add the word and its definitions at once
            description_formset = DefinitionInlineFormSet(request.POST, instance=created_word)
            if description_formset.is_valid():
                # If word and its descriptions are valid, save objects
                created_word.save()
                description_formset.save()
                # Redirect to show the new/edited word
                context = {'word': created_word, 'definitions': created_word.definition_set.all()}
                return render(request, 'words/show.html', context)
        else:
            # If word_form is not valid, we must create inline formset with the previous word to render it again
            description_formset = DefinitionInlineFormSet(request.POST, instance=word)
    else:
        # Create empty forms        
        word_form = WordForm(instance=word)
        description_formset = DefinitionInlineFormSet(instance=word)
    return render(request, 'words/add_edit.html', {'word_form': word_form, 'description_formset': description_formset})