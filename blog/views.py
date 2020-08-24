from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    allArticles = Article.objects.all()
    context = {
        'articles': allArticles,
    }
    return render(request, 'index.html', context)

# Create your views here.
