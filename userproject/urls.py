from userproject.views import LikeView, LikeUpdateView
from django.urls import path

urlpatterns = [
    path('likes/', LikeView.as_view()),  
    path('likes/<str:pk>', LikeUpdateView.as_view()),
    ]