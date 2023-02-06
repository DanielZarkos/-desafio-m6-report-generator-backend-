from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view(), name='contact-list'),
]
