from django.shortcuts import render
from .models import PrimaryDevice
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrimaryDeviceSerializer

class PrimaryDeviceDetails(APIView):
    permission_classes = [AllowAny] 
    def get(self,request, format=None):
        user = request.data['user']
        device = PrimaryDevice.objects.get(user = user)
        serializer = PrimaryDeviceSerializer(device)
        return Response({'details': serializer.data}, status = status.HTTP_200_OK)

    
    def post(self, request, format=None):
        user = request.data['user']
        serializer = PrimaryDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        user = request.data['user']
        device = PrimaryDevice.objects.get(user=user)
        serializer = PrimaryDeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)