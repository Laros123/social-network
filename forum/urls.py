from django.contrib import admin
from django.urls import path
from .views import BranchDetailView, BranchListView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branch/<int:pk>', BranchDetailView.as_view(), name='branch-detail'),
]
