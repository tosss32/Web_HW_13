from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializer import AuthorSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializer import UserRegistrationSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_authors(request):
    queryset = Author.objects.all()

    serializer = AuthorSerializer(queryset, many=True)


    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_password_reset_email(user, token):
    subject = 'Password Reset'
    message = render_to_string('password_reset_email_template.html', {'user': user, 'token': token})
    plain_message = strip_tags(message)
    from_email = 'alya.v.kravchenko@gmail.com' 
    to_email = user.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=message)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]