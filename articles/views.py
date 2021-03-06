from django.shortcuts import render
from . import models


def articles_lists(request):
    articles = models.Article.objects.all().order_by('-date')

    args = {
        'articles': articles
    }
    return render(request, 'articles/articleslist.html', args)


def articles_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})
