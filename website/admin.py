from django.contrib import admin
from website.models import NewsItem, ImageItem, Author, Source


admin.site.register(NewsItem)
admin.site.register(ImageItem)
admin.site.register(Author)
admin.site.register(Source)

