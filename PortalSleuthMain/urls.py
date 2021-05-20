from django.urls import path
from .views import (
ReviewDetailView,
ReviewCreateView,
ReviewUpdateView,
ReviewDeleteView,
# EmojiReviewCreateView,
EmojiReviewAddedView
# EmojiReviewDetailView
)
from . import views

urlpatterns = [
    path('', views.home, name='PortalSleuth-home'),
    path('contact/',views.contact, name='PortalSleuth-contact'),

    path('home/',views.home, name='PortalSleuth-home'),
    path('review/',views.review, name='PortalSleuth-review'),
    path('chooseReview/',views.chooseReview, name='PortalSleuth-chooseReview'),
    path('category/',views.category, name='PortalSleuth-category'),
    path('review/<int:pk>/',ReviewDetailView.as_view(template_name='PortalSleuthMain/detailReview.html'), name='submit-review'),
    path('review/new/',ReviewCreateView.as_view(template_name='PortalSleuthMain/addReview.html'), name='new-review'),
    path('review/<int:pk>/update/',ReviewUpdateView.as_view(template_name='PortalSleuthMain/addReview.html'), name='update-review'),
    path('review/<int:pk>/delete/',ReviewDeleteView.as_view(template_name='PortalSleuthMain/deleteReview.html'), name='delete-review'),
    path('livefeed/',views.livefeed, name='livefeed'),
    # path('getVideo/<int:pk>',views., name='livefeedSelectEmoji'),
    path('getVideo/',views.getVideo, name='getVideo'),
    path('selectFrame/',views.selectFrame, name='selectFrame'),
    path('submittedEmoji/',views.submittedEmoji, name='submittedEmoji'),
    # path('getLastFrameEmotion/',views.getLastFrameEmotion, name='lastFrame'),
]
