from django.urls import path

from flow_manager.views.ListIPbyFlow import IPListAPIView
from .views import IP, FLowListCreate, FLowRetrieveUpdate, IPListCreate, IPRetrieveUpdate, DeleteIP, DeleteFlow

urlpatterns = [
    path('flows/', FLowListCreate.as_view(), name='flow-list-create'),
    path('flows/<int:pk>/', FLowRetrieveUpdate.as_view(), name='flow-detail'),
    path('flows/<int:flow_id>/ips/', IPListAPIView.as_view(), name='ip-list'),
    path('flows/delete/<int:flow_id>/', DeleteFlow.as_view(), name='delete-flow'),
    path('ips/', IPListCreate.as_view(), name='ip-list-create'),
    path('ips/<int:pk>/', IPRetrieveUpdate.as_view(), name='ip-detail'),
    path('ips/delete/<int:flow>/<str:ip>/', DeleteIP.as_view(), name='ip-list'),
]
