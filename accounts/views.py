from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from django.conf import settings
import json
import os
User = get_user_model()

class Profile(APIView):
	permission_classes = [AllowAny] 
	def get(self, request, format=None):
		user = User.objects.get(id = request.headers['Authorization'])
		user_details = {
			'first_name': user.first_name,
			'last_name':user.last_name,
			'email': user.email,
		}
		profile = UserProfile.objects.get(user_id=request.headers['Authorization'])
		serializer = UserProfileSerializer(profile)
		return Response({'profile': serializer.data, 'user_details': user_details}, status=status.HTTP_200_OK)

	def put(self, request, format=None):
		user = User.objects.get(id = request.headers['Authorization'])
		user_details = {
			'first_name': user.first_name,
			'last_name':user.last_name,
			'email': user.email,
		}
		profile = UserProfile.objects.get(user_id=request.headers['Authorization'])
		request.data['user'] = request.headers['Authorization'] #Passing user id
		serializer = UserProfileSerializer(profile, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'profile': serializer.data, 'user_details': user_details}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Generate(APIView):
	permission_classes = [AllowAny]
	def post(self, request, format=None):
		user = User.objects.get(email=request.data['email'])
		config={
			"username":user.email,
			"password":request.data['password'],
			"first_name":user.first_name,
			"last_name":user.last_name,
			"isLoggedIn":False,
			"type":"primary",
			"user_id":user.id,
		}
		filename = str(user.email.split('@')[0])+".json"
		with open(os.path.join(settings.MEDIA_ROOT, f'{filename}'), 'w') as output:
			json.dump(config, output)

		return Response({'link': f'http://localhost:8000/media/{filename}'}, status=status.HTTP_201_CREATED)

	def delete(self, request, format=None):
		permission_classes = [AllowAny]
		user = User.objects.get(email=request.data['email'])
		filename = str(user.username.split('@')[0])+".json"
		os.remove(os.path.join(settings.MEDIA_ROOT, f'{filename}'))
		return Response(status=status.HTTP_200_OK)



class VerifyPassword(APIView):
	permission_classes = [AllowAny]
	def post(self, request, format=None):
		user = User.objects.get(id=request.headers['Authorization'])
		check = user.check_password(request.data['old_password'])
		if check:
			return Response(status=status.HTTP_200_OK)
		return Response(status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

