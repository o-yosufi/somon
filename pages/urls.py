from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]