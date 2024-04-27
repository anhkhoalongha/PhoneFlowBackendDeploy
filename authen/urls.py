from django.urls import path

from .views import KeyAuthentication, Logout

urlpatterns = [
    path('key-active/', KeyAuthentication.as_view(), name='authen-key-active'),
    path('logout/<str:token>/', Logout.as_view(), name='logout-key-active'),
]