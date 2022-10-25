from django.urls import path
from . import views

urlpatterns = [
    path('', views.username_or_password),
]