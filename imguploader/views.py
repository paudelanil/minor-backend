from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ImgUploadSerializer
from .models import Img

# Create your views here.
class ImgViewset(viewsets.ModelViewSet):
    queryset=Img.objects.all()
    serializer_class=ImgUploadSerializer