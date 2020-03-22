from django.urls import path
from .views import (
ReviewDetailView,
ReviewCreateView,
ReviewUpdateView,
ReviewDeleteView
)
from . import views

urlpatterns = [
    path('', views.review, name='PortalSleuth-review'),
    # path('about/',views.about, name='PortalSleuth-about'),
    # path('home/',views.home, name='PortalSleuth-home'),
    path('review/',views.review, name='PortalSleuth-review'),

    path('review/<int:pk>/',ReviewDetailView.as_view(template_name='PortalSleuthMain/detailReview.html'), name='submit-review'),
    path('review/new/',ReviewCreateView.as_view(template_name='PortalSleuthMain/addReview.html'), name='new-review'),
    path('review/<int:pk>/update/',ReviewUpdateView.as_view(template_name='PortalSleuthMain/addReview.html'), name='update-review'),
    path('review/<int:pk>/delete/',ReviewDeleteView.as_view(template_name='PortalSleuthMain/deleteReview.html'), name='delete-review'),

]
