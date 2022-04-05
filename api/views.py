from django.shortcuts import render
from api.serializers import CustomUserModelSerializer, CustomUserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView, status


class ModelSView(APIView):
    def post(self, request):
        serializer = CustomUserModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )


class SerializerView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
