from django.urls import path
from . import views
from .views import text


urlpatterns = [
    path('text/', text)
]