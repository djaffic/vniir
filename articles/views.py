from django.shortcuts import render, get_object_or_404
from articles.models import Tag, Article, Partner
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

#Вьюшка для вывода списка статей
def articles_list(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'articles': articles
    }
    return render(request, "articles/articles_list.html", context)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {
        'article': article
    }
    return render(request, "articles/article_detail.html", context)


def last_articles(request):
    ordered_articles = Article.objects.order_by('-pub_date')[:3]
    last_article = Article.objects.last()
    partners = Partner.objects.all()
    context = {
        'ordered_articles': ordered_articles,
        'last_article': last_article,
        'partners': partners
    }
    return render(request, "index.html", context)


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, "articles/tags_list.html", context)


def tag_detail(request, pk):
    tag = Tag.objects.get(id=pk)
    context = {
        'tag': tag
    }
    return render(request, 'articles/tag_detail.html', context)
