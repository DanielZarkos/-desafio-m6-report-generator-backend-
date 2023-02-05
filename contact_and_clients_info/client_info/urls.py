from django.urls import path
from .views import ClientList
from .serializers import ClientSerializer
from . import views

urlpatterns = [
    path('clients/', views.ClientList.as_view(), name='client-list'),
]
