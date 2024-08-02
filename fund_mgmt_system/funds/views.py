from django.shortcuts import render
from rest_framework import viewsets
from .models import Fund
from .serializers import FundSerializers

# Create your views here.

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializers