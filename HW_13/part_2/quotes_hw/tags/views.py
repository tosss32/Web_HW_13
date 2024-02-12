from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tag
from .serializer import TagSerializer

@api_view(['GET'])
def list_tags(request):
    queryset = Tag.objects.all()

    serializer = TagSerializer(queryset, many=True)


    return Response(serializer.data)
