from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import IP
from ..serializers import IPSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class IPListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ips = IP.objects.all()
        serializer = IPSerializer(ips, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IPRetrieveUpdate(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(IP, pk=pk)

    def get(self, request, pk):
        ip = self.get_object(pk)
        serializer = IPSerializer(ip)
        return Response(serializer.data)

    def put(self, request, pk):
        ip = self.get_object(pk)
        serializer = IPSerializer(ip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        ip = self.get_object(pk)
        serializer = IPSerializer(ip, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteIP(APIView):
    permission_classes = [AllowAny]

    def get_object(self, flow, ip):
        try:
            return IP.objects.get(flow=flow, ip=ip)
        except IP.DoesNotExist:
            raise Http404

    def delete(self, request, flow, ip):
        ip_obj = self.get_object(flow=flow, ip=ip)
        ip_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
