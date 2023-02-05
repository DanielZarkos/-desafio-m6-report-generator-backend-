from django.urls import path
from .views import ClientList
from .serializers import ClientSerializer

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
]
