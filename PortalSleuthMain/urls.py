from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='PortalSleuth-home'),
    path('home/',views.home, name='PortalSleuth-home'),
]
