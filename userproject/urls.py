from userproject.views import ProjectView, ProjectUpdateView, EducationView, EducationUpdateView, ExperienceView, ExperienceUpdateView
from django.urls import path

urlpatterns = [
    path('project/', ProjectView.as_view()),  
    path('project/<str:pk>', ProjectUpdateView.as_view()),

    path('education/', EducationView.as_view()),
    path('education/<str:pk>', EducationUpdateView.as_view()),

    path('experience/', ExperienceView.as_view()),
    path('experience/<str:pk>', ExperienceUpdateView.as_view()),
    ]