from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Linkman
from .serializers import LinkmanSerializer

# Create your views here.

class LinkmanViewSet(viewsets.ModelViewSet):
    queryset = Linkman.objects.all()
    serializer_class = LinkmanSerializer
    permission_classes = [permissions.IsAuthenticated]