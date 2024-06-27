from django.contrib import admin
from django.urls import path
from .views import BranchDetailView, BranchListView, PostDetailView, CommentaryCreateView, PostCreateView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branch/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branch/<int:pk>/post-create/', PostCreateView.as_view(), name='post-create'),
    path('branch/<int:bk>/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('branch/<int:bk>/post/<int:pk>/create-commentary/<int:cr>', CommentaryCreateView.as_view(), name='comment-create'),
]
