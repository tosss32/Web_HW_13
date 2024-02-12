from rest_framework import routers
from .views import QuoteViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', QuoteViewSet)

urlpatterns = [
    # ...
    path('', include(router.urls)),
    # ...
]