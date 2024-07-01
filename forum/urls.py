from django.contrib import admin
from django.urls import path
from .views import BranchDetailView, BranchListView, PostDetailView, CommentaryCreateView, PostCreateView, PostDeleteView, CommentDeleteView, GradeCreateView, grade_get_view

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branch/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branch/<int:pk>/post-create/', PostCreateView.as_view(), name='post-create'),
    path('branch/<int:bk>/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('branch/<int:bk>/post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('branch/<int:bk>/post/<int:pk>/comment/<int:cr>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('branch/<int:bk>/post/<int:pk>/comment/<int:cr>/create', CommentaryCreateView.as_view(), name='comment-create'),
    path('rating/', GradeCreateView.as_view(), name='rating'),
    path('rating-comment/', grade_get_view, name='rating'),
]
