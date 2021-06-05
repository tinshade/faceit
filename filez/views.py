from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import FilesData
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import FilezDataSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


User = get_user_model()


class FileActions(APIView):
	permission_classes = [AllowAny] 
	def get(self, request, format=None):
		user_id = request.headers["Authorization"]
		filez_stream = FilesData.objects.all()
		data = request.headers['Authorization'].split('&')
		if len(data)>1:
			filez = filez_stream.filter(user_id=int(data[0]), month=str(data[1]))
		else:
			filez = filez_stream.filter(user_id=int(data[0]))
		#filez = filez_stream.filter(user_id=user_id)
		serializer = FilezDataSerializer(filez, many=True)
		#print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		if request.data['purge_scheduled'] == 1:
			request.data['purge_scheduled'] = True
		elif request.data['purge_scheduled'] == 0:
			request.data['purge_scheduled'] = False
		serializer = FilezDataSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, format=None):
		filez = FilesData.objects.get(user_id = request.headers["Authorization"], file_id = request.data['file_id'])
		serializer = FilezDataSerializer(filez, data={'purge_scheduled': request.data['purge_scheduled']}, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_200_OK)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		filez = FilesData.objects.get(file_id = request.data['file_id'])
		filez.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)