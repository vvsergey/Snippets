from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})


def snippets_page(request):
    form = SnippetForm()
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов', 'snippets': snippets, 'form': form}
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    context = {'pagename': 'Страница сниппета', 'snippet': snippet}
    return render(request, 'pages/snippet_detail.html', context)


def create_snippet(request):
   if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("redirect_url")
       return render(request, 'add_snippet.html', {'form': form})


def snippets_page(request):
   form = SnippetForm()
   return render(request, 'add_snippet.html', {'form': form})