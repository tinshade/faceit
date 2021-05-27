from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import DeviceData
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeviceDataSerializer


User = get_user_model()


class DeviceDetails(APIView):
    permission_classes = [AllowAny] 
    def get(self,request, format=None):
        user = request.data['user']
        device = DeviceData.objects.get(user = user)
        serializer = DeviceDataSerializer(device)
        return Response({'details': serializer.data}, status = status.HTTP_200_OK)

    
    def post(self, request, format=None):
        user = request.data['user']
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        user = request.data['user']
        device = DeviceData.objects.get(user=user)
        serializer = DeviceDataSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

