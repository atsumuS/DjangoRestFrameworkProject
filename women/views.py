from urllib import response
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .models import Category, Women
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import WomenSerializer
from women import serializers
from rest_framework import status
from rest_framework import viewsets
from .permissions import *
from rest_framework.authentication import TokenAuthentication




class WomenApiList(generics.ListCreateAPIView): 
        queryset = Women.objects.all()
        serializer_class = WomenSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        

class WomenApiUpdate(generics.RetrieveUpdateDestroyAPIView):
        queryset = Women.objects.all()
        serializer_class = WomenSerializer
        permission_classes = [ListAloowEditAuth]
        
        

class WomenAPIdelete(generics.RetrieveDestroyAPIView):
        queryset = Women.objects.all()
        serializer_class = WomenSerializer 
        permission_classes = [DeleteAdminGetAllow]

