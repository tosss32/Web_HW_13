
from rest_framework import viewsets
from .models import Quote
from .serializer import QuoteSerializer
from rest_framework import permissions

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]