from django.urls import path
from . import views
from jobapp.views import text


urlpatterns = [
    path('job_advert/create/', views.jobadvert_create_view, name='job_advert'),
    path('job_advert/<slug:slug_company>=<slug:slug_title>/', views.jobadvert_detail_view, name='job_advert_detail'),
    # path('job_advert/<slug:slug_company>=<slug:slug_title>/update/', views.jobadvert_update_view, name='job_advert_upate'),
    path('job_advert/<slug:slug>/application', views.jobadvert_create_view, name='job_application'),
]