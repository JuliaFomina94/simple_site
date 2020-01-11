from django.contrib import admin
from django.urls import path, include
from website.views import home, news, newsitem


urlpatterns = [
    path('home/', home, name="homepage"),
    path('news/', news),
    path('news/<int:newsitem_id>', newsitem, name="newsitem")
]

