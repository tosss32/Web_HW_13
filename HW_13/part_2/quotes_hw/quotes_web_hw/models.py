from django.db import models

from django.db import models
from autors.models import Author
from tags.models import Tag

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'quotes_web_hw'

