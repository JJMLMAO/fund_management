from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fund
from .serializers import FundSerializers

# Create your views here.

class TestAPIView(APIView):
    def get(self, request):
        print('hi i am test Api bro')
        return Response({"message": "Hello from Django!"}, status=status.HTTP_200_OK)

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializers
    

