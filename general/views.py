from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, FormView, CreateView, UpdateView

from general.forms import NewPostForm
from general.models import JobPost, Category
from general.models import *


class MainView(ListView):
    paginate_by = 4
    model = JobPost
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        cats = Category.objects.all()
        locations = Location.objects.all()
        last_posts = JobPost.objects.all()
        last_posts_amount = last_posts.count()
        tags = Tag.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['last_posts'] = last_posts
        context['last_posts_amount'] = last_posts_amount
        context['tags'] = tags

        return context

    def get_queryset(self, *args, **kwargs):
        all_posts = super().get_queryset(*args, **kwargs)
        search_query = self.request.GET.get('search')
        location_query = self.request.GET.get('location')
        category_query = self.request.GET.get('category')
        tags_query = self.request.GET.get('tags')

        if location_query:
            return all_posts.filter(
                                    title__contains=search_query,
                                    location__name=location_query,
                                    category__name=category_query,
                                    )

        return all_posts.order_by('published_date')


class PostDetailView(DetailView):
    model = JobPost
    template_name = 'main/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        cats = Category.objects.all()
        locations = Location.objects.all()
        tags = Tag.objects.all()
        posts = JobPost.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags
        context['posts'] = posts

        return context


class AddNewPost(CreateView):
    model = JobPost
    form_class = NewPostForm
    template_name = 'main/post_add.html'
    context_object_name = 'posts'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super(AddNewPost, self).get_context_data(**kwargs)

        cats = Category.objects.all()
        locations = Location.objects.all()
        tags = Tag.objects.all()
        posts = JobPost.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags
        context['posts'] = posts

        return context


class PostEdit(UpdateView):
    model = JobPost
    template_name = 'main/post_add.html'
    context_object_name = 'post'
    form_class = NewPostForm

    def form_valid(self, form):
        if self.request.user == form.instance.author:
            return super().form_valid(form)
        else:
            return redirect('index')

    def get_context_data(self, **kwargs):
        context = super(PostEdit, self).get_context_data(**kwargs)
        return context


class PostCategoryView(ListView):
    model = JobPost
    template_name = 'main/category.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCategoryView, self).get_context_data(**kwargs)

        cats = Category.objects.all()
        locations = Location.objects.all()
        tags = Tag.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        return JobPost.objects.filter(category__slug=slug)


class PostLocationView(ListView):
    model = JobPost
    template_name = 'main/category.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostLocationView, self).get_context_data(**kwargs)

        cats = Category.objects.all()
        locations = Location.objects.all()
        tags = Tag.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        return JobPost.objects.filter(location__slug=slug)


class PostTagsView(ListView):
    model = JobPost
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return JobPost.objects.filter(tags__slug=slug)

    def get_context_data(self, **kwargs):
        context = super(PostTagsView, self).get_context_data(**kwargs)
        cats = Category.objects.all()
        locations = Location.objects.all()
        last_posts = JobPost.objects.filter()
        last_posts_amount = last_posts.count()
        tags = Tag.objects.all()
        posts = JobPost.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['last_posts_amount'] = last_posts_amount
        context['tags'] = tags
        context['posts'] = posts

        return context


class AboutUsView(View):
    def get(self, request):
        return render(request, 'main/about-us.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class ElementsView(View):
    def get(self, request):
        return render(request, 'main/elements.html')


class PriceView(View):
    def get(self, request):
        return render(request, 'main/price.html')


