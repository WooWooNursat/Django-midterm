from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from main.models import Book, Journal
from main.serializers import BookSerializer, JournalSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated, )
        else:
            permission_classes = (IsAdminUser, )
        return [permission() for permission in permission_classes]


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]
