from django.contrib import admin
from django.urls import path
from .views import BranchDetailView, BranchListView, PostDetailView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branch/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
