from django.urls import path
from . import views

urlpatterns = [
    path('', views.evina),
    path('evina', views.evina),
    ]
