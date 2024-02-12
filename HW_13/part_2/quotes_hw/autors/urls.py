
from .views import list_authors
from django.urls import path
from .views import reset_password


urlpatterns = [
    path('', list_authors),
    path('reset-password/', reset_password, name='reset-password'),
  
]