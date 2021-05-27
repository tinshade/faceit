from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Pseudousers
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import PseudoSerializer


User = get_user_model()


class Pseudo(APIView):
	permission_classes = [AllowAny] 
	def get(self, request, format=None):
		user = User.objects.get(id=request.headers['Authorization'])
		pseudousers = Pseudousers.objects.all()
		pseudousers.filter(user_id=request.headers['Authorization'])
		serializer = PseudoSerializer(pseudousers, many=True)
		return Response({'pseudoers': serializer.data}, status=status.HTTP_200_OK)


	def post(self, request, format=None):
		user = User.objects.get(id=request.headers['Authorization'])
		request.data['user'] = request.headers['Authorization']
		serializer = PseudoSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		pseudoer = Pseudousers.objects.get(id=request.data['id'])
		pseudoer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, format=None):
		pseudoer = Pseudousers.objects.get(id = request.data['id'], user_id = request.data['user'])
		serializer = PseudoSerializer(pseudoer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PseudoAuth(APIView):
	permission_classes = [AllowAny]

	def post(self, request, format=None):
		user_id = request.headers['Authorization']
		username = request.data['username']
		password = request.data['password']
		pseudoer = Pseudousers.objects.get(user_id=user_id, username=username)
		print(pseudoer.password, password)
		if password == pseudoer.password:
			return Response(status = status.HTTP_200_OK)
		return Response(status = status.HTTP_401_UNAUTHORIZED)


