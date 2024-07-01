from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from .forms import CommentaryCreationForm, PostCreateForm
from .models import Branch, Post, Commentary, Rating, Grade

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
        context['user_thumb'] = self.object.rating.grades.filter(user=self.request.user).last()
        return context
    
class CommentDeleteView(View):
    model = Commentary

    def post(self, request, *args, **kwargs):
        commentary = self.model.objects.get(pk=self.kwargs.get('cr'))
        commentary.delete()

        return HttpResponseRedirect(commentary.post.get_absolute_url())

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

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            comment.author = request.user
            comment.post = self.get_post()
            if self.kwargs.get('cr'):
                comment.commentary = self.get_comment()
            comment.save()
            rating = Rating.objects.create()
            comment.rating = rating
            comment.save()

        return HttpResponseRedirect(comment.post.get_absolute_url())
    
class PostDeleteView(View):
    model = Post

    def post(self, request, *args, **kwargs):
        post_object = self.model.objects.get(pk=self.kwargs.get('pk'))
        post_object.delete()

        return HttpResponseRedirect(post_object.branch.get_absolute_url())

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
            rating = Rating.objects.create()
            post_object.rating = rating
            post_object.save()

        return HttpResponseRedirect(post_object.get_absolute_url())


class GradeCreateView(View):
    model = Grade
    
    def post(self, request, *args, **kwargs):
        rating = request.POST.get('rating')
        value = int(request.POST.get('value'))
        user = request.user if request.user.is_authenticated else None
        grade, created = self.model.objects.get_or_create(
            rating=Rating.objects.get(pk=rating),
            user = user,
            defaults={'value': value},
        )
        
        if not created:
            if grade.value == value:
                grade.delete()
                return JsonResponse({'status': 'deleted', 'rating_sum': grade.rating.get_rating(), 'grade': 0})
            else:
                grade.value = value
                grade.user = user
                grade.save()
                return JsonResponse({'status': 'updated', 'rating_sum': grade.rating.get_rating(), 'grade': grade.value})
        return JsonResponse({'status': 'created', 'rating_sum': grade.rating.get_rating(), 'grade': grade.value})
    
def grade_get_view(request):
    comment = Commentary.objects.get(pk=request.GET.get('comment'))
    grade = comment.rating.grades.all().filter(user=request.user).last()
    if grade:
        return JsonResponse({'grade': grade.value})
    return JsonResponse({'grade': 0})