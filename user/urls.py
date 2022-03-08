from django.urls import path
from user.views import *

urlpatterns = [
    path('logout/', logout_user, name='logoutfunc'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('other-profile/<int:pk>', OtherProfileView.as_view(), name='other-profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile')
]