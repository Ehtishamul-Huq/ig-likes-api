from django.conf.urls import url
from user.views import UserRegistrationView, UserLoginView
from django.urls import path

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    ]