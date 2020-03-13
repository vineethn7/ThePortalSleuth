from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='PortalSleuth-home'),
    path('about/',views.about, name='PortalSleuth-about'),
    path('home/',views.home, name='PortalSleuth-home'),
    path('review/',views.review, name='PortalSleuth-review'),
    path('post/',views.post, name='PortalSleuth-post'),

]
