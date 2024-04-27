from rest_framework import generics
from ..models import IP
from ..serializers import IPSerializer

class IPListAPIView(generics.ListAPIView):
    serializer_class = IPSerializer

    def get_queryset(self):
        flow_id = self.kwargs.get('flow_id')
        return IP.objects.filter(flow_id=flow_id)