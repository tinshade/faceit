from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Inquiry
from .serializers import AskSerializer

class Ask(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = AskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
