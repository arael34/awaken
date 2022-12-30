from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', login_required(views.logout_view), name='logout'),
    path('profile/', login_required(views.profile_view), name='profile'),
]
