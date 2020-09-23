from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import Definition, Word
from .forms import WordForm

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
    # Get all definitions of selected word
    definitions = Definition.objects.filter(word__name = word)
    # Add word and definitions to context to send them to the template
    context = {'word': word, 'definitions': definitions}
    return render(request, 'words/show.html', context)

def delete(request, word):
    # Remove word and its definitions and go to homepage
    Word.objects.filter(name=word).delete()    
    return redirect('/')

def add(request):
    # Create an inline formset to add the word and its definitions at once
    DefinitionInlineFormSet = inlineformset_factory(Word, Definition, fields=('description',))
    if request.method == 'POST':
        # Process sent data
        word_form = WordForm(request.POST)
        if word_form.is_valid():            
            created_word = word_form.save(commit=False)
            description_formset = DefinitionInlineFormSet(request.POST, instance=created_word)
            if description_formset.is_valid():
                # If word and its descriptions are valid, save objects
                created_word.save()
                description_formset.save()
                return redirect('/')
        else:
            # If word_form is not valid, we must create inline formset with a new word instance 
            word = Word()
            description_formset = DefinitionInlineFormSet(request.POST, instance=word)
    else:
        # Create empty forms
        word = Word()
        word_form = WordForm(instance=word)
        description_formset = DefinitionInlineFormSet(instance=word)
    return render(request, 'words/add.html', {'word_form': word_form, 'description_formset': description_formset})

def edit(request, word):
    DefinitionInlineFormSet = inlineformset_factory(Word, Definition, fields=('description',))
    if request.method == 'POST':
        # Process sent data
        word = Word.objects.get(name=word)
        word_form = WordForm(request.POST, instance=word)
        if word_form.is_valid():            
            created_word = word_form.save(commit=False)
            description_formset = DefinitionInlineFormSet(request.POST, instance=created_word)
            if description_formset.is_valid():
                # If word and its descriptions are valid, save objects
                created_word.save()
                description_formset.save()
                return redirect('/')
        else:
            # If word_form is not valid, we must create inline formset with a new word instance 
            description_formset = DefinitionInlineFormSet(request.POST, instance=word)
    else:
        # Create empty forms
        word = Word.objects.get(name=word)
        word_form = WordForm(instance=word)
        description_formset = DefinitionInlineFormSet(instance=word)
    return render(request, 'words/edit.html', {'word_form': word_form, 'description_formset': description_formset})

