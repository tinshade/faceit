from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Threat
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ThreatSerializer

User = get_user_model()


class ThreatActions(APIView):
	permission_classes = [AllowAny] 
	def get(self, request, format=None):
		user_id = request.headers["Authorization"]
		threat_stream = Threat.objects.all()
		data = request.headers['Authorization'].split('&')
		if len(data)>1:
			threat = threat_stream.filter(user_id=int(data[0]), month=str(data[1]))
		else:
			threat = threat_stream.filter(user_id=int(data[0]))
		serializer = ThreatSerializer(threat, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = ThreatSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, format=None):
		threat = Threat.objects.get(user_id = request.headers["Authorization"], pk = request.data['threat_id'])
		serializer = ThreatSerializer(threat, data={'threat_name': request.data['threat_name']}, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_200_OK)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, format=None):
	# 	threat = Threat.objects.get(id = request.data['threat_id'])
	# 	threat.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)