from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from .forms import CommentaryCreationForm, PostCreateForm
from .models import Branch, Post, Commentary

# Create your views here.


class BranchListView(ListView):
    model = Branch
    template_name = "forum/branch-list.html"
    context_object_name = 'branches'

class BranchDetailView(DetailView):
    model = Branch
    template_name = "forum/branch-detail.html"
    context_object_name = 'branch'

class PostDetailView(DetailView):
    model = Post
    template_name = "forum/post-detail.html"
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentaryCreationForm()
        post = self.get_object()
        context['comments'] = Commentary.objects.filter(post=post, commentary__isnull=True)
        return context

class CommentaryCreateView(View):
    form_class = CommentaryCreationForm

    def get_post(self, **kwargs):
        post_id = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=post_id)
    
    def get_comment(self, **kwargs):
        comment_id = self.kwargs.get('cr')
        return get_object_or_404(Commentary, pk=comment_id)
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentaryCreationForm(request.POST, request.FILES)
        print(comment_form)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            comment.author = request.user
            comment.post = self.get_post()

            print(self.kwargs.get('cr'))
            if self.kwargs.get('cr'):
                comment.commentary = self.get_comment()

            comment.save()

        return HttpResponseRedirect(comment.post.get_absolute_url())

class PostCreateView(TemplateView):
    template_name = "forum/post-create.html"
    form_class = PostCreateForm

    def get_branch(self):
        return get_object_or_404(Branch, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_object = post_form.save(commit=False)

            post_object.author = request.user
            post_object.branch = self.get_branch()

            post_object.save()

        return HttpResponseRedirect(post_object.get_absolute_url())
