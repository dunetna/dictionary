from django.shortcuts import render
from .models import Word

def index(request):
    # Get partial or complete word to find
    search = request.GET.get('search')
    # Get all words starting with string introduced by user
    words = list(Word.objects.filter(name__startswith=search))
    # Send all words to the template
    context = {'words': words}
    return render(request, 'words/index.html', context)