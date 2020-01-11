from django.db import models
from uuid import uuid4

def get_filepath(instance, filepath):
    extension = filepath.split(".")[-1]
    folders = {
        ImageItem: "Image"
    }
    print(type(instance))
    filepath = f"{folders.get(type(instance), 'other')}/{uuid4()}.{extension}"
    return filepath

class NewsItem(models.Model):
    title = models.CharField("Заголовок", max_length=255, default="<<No title>>", null=False, blank=False)
    short_description = models.CharField("Описание", max_length=1024, default="<<No description>>", null=False, blank=False)
    published = models.DateTimeField("Дата публикации", auto_now=True)
    content = models.TextField("Текст статьи", default="<<No text>>", null=False, blank=False)
    preview_image = models.ForeignKey("ImageItem", on_delete=models.SET_NULL, null=True, related_name="newsitem")
    illustration = models.ManyToManyField("ImageItem", related_name="newsitems")
    author = models.ManyToManyField("Author")
    source = models.ForeignKey("Source", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        name = f"id: {self.id} | date: {self.published} | title: {self.title}"
        return name

    class Meta:
        ordering = ["-id"]

class ImageItem(models.Model):
    title = models.CharField("Название картинки", max_length=255, default="<<No title>>", null=False, blank=False)
    description = models.CharField("Описание", max_length=1024, default="<<No description>>", null=False, blank=False)
    image = models.ImageField(upload_to=get_filepath)


class Author(models.Model):
    first_name = models.CharField(max_length=255, default="<<No author>>", null=False, blank=False)
    middle_name = models.CharField(max_length=255, default="<<No author>>", null=False, blank=False)
    last_name = models.CharField(max_length=255, default="<<No author>>", null=False, blank=False)
    created = models.DateTimeField(auto_now=True)

    def get_shortname(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

class Source(models.Model):
    name = models.CharField(max_length=255, default="<<No author>>", null=False, blank=False)
    url = models.URLField(default="Simple site")

