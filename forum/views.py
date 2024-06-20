from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Branch, Post

# Create your views here.


class BranchListView(ListView):
    model = Branch
    template_name = "forum/branch-list.html"
    context_object_name = 'branches'

class BranchDetailView(DetailView):
    model = Branch
    template_name = "forum/branch-detail.html"
    context_object_name = 'branch'
 