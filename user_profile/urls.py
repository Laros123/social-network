from django.contrib import admin
from django.urls import path, include, re_path
from .views import ProfileDetailView, SettingsView

urlpatterns = [
    re_path(r'^profile/(?P<pk>\d+)(?:/(?P<ac>\w+))?/$', ProfileDetailView.as_view(), name='profile'),
    path('settings/<int:pk>', SettingsView.as_view(), name='settings')
]
