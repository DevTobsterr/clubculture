from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.application_home, name="application_home"),
]
