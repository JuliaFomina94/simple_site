from django.shortcuts import render, redirect
from website.models import NewsItem
from django.http import Http404


def redirect_to_home(request):
    return redirect("homepage")


def home(request):
    return render(request, 'website/home.html')


def news(request):
    news_item = NewsItem.objects.all()
    return render(request, 'website/news.html', {"news_item": news_item})


def newsitem(request, newsitem_id):
    news_item = NewsItem.objects.filter(id=newsitem_id).first()
    if not news_item:
        raise Http404
    return render(request, 'website/newsitem.html', {"news_item": news_item})
