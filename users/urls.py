from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CreationForm
from .views import RegisterView, ProfileView, profile2

app_name = 'users'

urlpatterns = [
    # path('auth/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html',
        next_page='users:profile2'), name='login'), #redirect_field_name # go to profile!
    path('logout/', LogoutView.as_view(template_name='users/logout.html',
        next_page='quizzes:index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('profile/', profile2, name='profile2'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
