from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerSerializer

class BannerListAPIView(ListAPIView): 
    queryset = Banner.objects.filter(is_show=True, is_deleted=False)
    
    serializer_class = BannerSerializer
