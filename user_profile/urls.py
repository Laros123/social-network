from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView

urlpatterns = [
    path('profile/<int:pk>/<str:ac>/', ProfileDetailView.as_view(), name='profile')
]
