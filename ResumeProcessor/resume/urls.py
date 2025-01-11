from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('api/extract_resume/', extract_resume,name="resume_extractor"),
]