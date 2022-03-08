from django.urls import path
from general.views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('single/<int:pk>/', PostDetailView.as_view(), name='single'),
    path('category/<slug:slug>/', PostCategoryView.as_view(), name='category'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('new-job-post/', AddNewPost.as_view(), name='new-job-post'),
    path('edit-post/<int:pk>', PostEdit.as_view(), name='edit-post'),
    path('tags/<slug:slug>/', PostTagsView.as_view(), name='tags'),
    path('location/<slug:slug>/', PostLocationView.as_view(), name='location')
]