
from .views import list_tags
from django.urls import path


urlpatterns = [
    # ...
    path('', list_tags),
    # ...
]