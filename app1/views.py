
from . models import Author, Poll
from rest_framework import generics
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from .serializer import *

class AuthorListCreate(views.APIView):

    def get(self, request, format=None):
        user = Author.objects.all()
        serializer = AuthorSerializer(user,many=True)
        return Response(serializer.data,status=200)


    