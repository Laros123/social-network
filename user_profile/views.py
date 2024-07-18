from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import Profile

# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile/profile-detail.html"
    context_object_name = 'profile'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        type_of_activity = self.kwargs.get('ac', 'none')
        if type_of_activity == 'posts':
            self.template_name = "profile/profile-detail-posts.html"
        elif type_of_activity == 'comments':
            self.template_name = "profile/profile-detail-comments.html"
        elif type_of_activity == 'upvoted':
            self.template_name = "profile/profile-detail-upvoted.html"
        elif type_of_activity == 'downvoted':
            self.template_name = "profile/profile-detail-downvoted.html"
        if type_of_activity == 'none':
            print(type_of_activity)
            
        return super().get(request, *args, **kwargs)

class SettingsView(DetailView):
    model = Profile
    template_name = "profile/settings.html"
    context_object_name = 'profile'