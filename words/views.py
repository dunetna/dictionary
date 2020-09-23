from django.shortcuts import render
from .models import Definition, Word

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