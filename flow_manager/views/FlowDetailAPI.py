from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import FLow
from ..serializers import FLowSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from authen.models import KeyActive

class FLowListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        key_active = KeyActive.objects.get(key=request.headers['Authorization'])
        project_ids_queryset = key_active.project.values_list('id', flat=True)
        project_ids_list = list(project_ids_queryset)
        flows = FLow.objects.filter(id__in=project_ids_list)
        serializer = FLowSerializer(flows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FLowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FLowRetrieveUpdate(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(FLow, pk=pk)

    def get(self, request, pk):
        flow = self.get_object(pk)
        serializer = FLowSerializer(flow)
        return Response(serializer.data)

    def put(self, request, pk):
        flow = self.get_object(pk)
        serializer = FLowSerializer(flow, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        flow = self.get_object(pk)
        serializer = FLowSerializer(flow, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        breakpoint()
        flow = self.get_object(pk)
        flow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteFlow(APIView):
    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        return get_object_or_404(FLow, pk=pk)
    
    def delete(self, request, flow_id):
        flow = self.get_object(flow_id)
        flow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)