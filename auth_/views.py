from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from auth_.models import MainUser
from auth_.serializer import MainUserSerializer
# Create your views here.



class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        if self.request.data.get('role') == 1:
            queryset = MainUser.objects.create_user(
                email=self.request.data.get('email'),
                password=self.request.data.get('password'),
            )
            serializer = MainUserSerializer(queryset)
            return Response(serializer.data)
        else:
            queryset = MainUser.objects.create_superuser(
                email=self.request.data.get('email'),
                password=self.request.data.get('password'),
            )
            serializer = MainUserSerializer(queryset)
            return Response(serializer.data)

