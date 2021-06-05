from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import ActivityLog
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ActivitySerializer

User = get_user_model()


class ActivityActions(APIView):
	permission_classes = [AllowAny] 
	def get(self, request, format=None):
		user_id = request.headers["Authorization"]
		act_stream = ActivityLog.objects.all()
		data = request.headers['Authorization'].split('&')
		if len(data)>1:
			act = act_stream.filter(user_id=int(data[0]), month=str(data[1]))
		else:
			act = act_stream.filter(user_id=int(data[0]))
		#act = act_stream.filter(user_id=user_id)
		serializer = ActivitySerializer(act, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = ActivitySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, format=None):
		threat = ActivityLog.objects.get(user_id = request.headers["Authorization"], month = request.data['month'])
		times_used = threat['times_used']+1
		serializer = ActivitySerializer(threat, data={'times_used': times_used}, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_200_OK)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, format=None):
	# 	threat = ActivityLog.objects.get(id = request.data['threat_id'])
	# 	ActivityLog.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)