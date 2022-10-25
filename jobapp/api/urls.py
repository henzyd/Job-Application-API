from django.urls import path
from . import views


urlpatterns = [
    path('job_advert/', views.jobadvert_create_view, name='job_advert')
]