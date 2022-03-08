from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from urllib3 import request
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import *
from hhsite import settings
from general.models import JobPost, Category, Location, Tag
from user.models import CustomUser


class LoginUser(LoginView):
    model = JobPost
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        posts = JobPost.objects.all()
        locations = Location.objects.all()
        cats = Category.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags
        context['posts'] = posts

        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


class RegisterView(CreateView):
    model = JobPost
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        posts = JobPost.objects.all()
        locations = Location.objects.all()
        cats = Category.objects.all()

        context['cats'] = cats
        context['locations'] = locations
        context['tags'] = tags
        context['posts'] = posts

        return dict(list(context.items()))


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super(ProfileView, self).get_context_data(**kwargs)
            posts = JobPost.objects.all()
            locations = Location.objects.all()
            cats = Category.objects.all()
            user_posts = JobPost.objects.filter(author=self.request.user)

            form_class = UserProfileForm
            context['posts'] = posts
            context['locations'] = locations
            context['cats'] = cats
            context['form'] = form_class
            context['user_posts'] = user_posts

            return context
        else:
            return redirect('login')

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)


class EditProfileView(UpdateView):
    model = CustomUser
    template_name = 'registration/edit_profile.html'
    context_object_name = 'user'
    form_class = UserProfileForm

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)
        else:
            return redirect('edit-profile')

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = super(EditProfileView, self).get_context_data(**kwargs)
            posts = JobPost.objects.all()
            locations = Location.objects.all()
            cats = Category.objects.all()
            user_posts = JobPost.objects.filter(author=self.request.user)

            context['posts'] = posts
            context['locations'] = locations
            context['cats'] = cats
            context['user_posts'] = user_posts

            return context

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)


class OtherProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/other_profile.html'
    context_object_name = 'user'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super(OtherProfileView, self).get_context_data(**kwargs)
            posts = JobPost.objects.all()
            locations = Location.objects.all()
            cats = Category.objects.all()
            form_class = UserProfileForm

            context['posts'] = posts
            context['locations'] = locations
            context['cats'] = cats
            context['form'] = form_class
            return context


