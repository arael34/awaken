from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .controllers import create_graph_div
from awaken.models import Points
from awaken.jobs import reset_points

def login_view(request):
    if request.user.is_authenticated: return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('signup') # tweak this later
    form = AuthenticationForm()
    return render(request, 'login.html', context = {"login_form": form})

def signup_view(request):
    if request.user.is_authenticated: return redirect('profile')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'signup.html', context = {"register_form": form})

def logout_view(request):
    logout(request)
    response = redirect('login')
    return response

def profile_view(request):
    user = request.user
    obj = Points.objects.get_or_create(user_id = user)[0]
    reset_points(user)

    daily_points, weekly_points = obj.daily_points, obj.weekly_points
    graph_div = create_graph_div(user)

    return render(request, 'profile.html', {
        'user': user,
        'daily_points': daily_points,
        'weekly_points': weekly_points,
        'graph_div': graph_div,
    })
