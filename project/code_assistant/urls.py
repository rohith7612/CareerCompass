from django.urls import path
from . import views

urlpatterns = [
    path('codesavant/', views.codesavant, name='codesavant'),
    path('run_code/', views.run_code, name='run_code'),
    path('assistant_feedback/', views.assistant_feedback, name='assistant_feedback'),
]