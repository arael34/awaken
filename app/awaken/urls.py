from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.view_tasks), name='index'),
    path('add/', login_required(views.create_task.as_view()), name='add'),
    path('<int:pk>/', login_required(views.edit_task.as_view()), name='task-edit'),
    path('<int:pk>/delete/', login_required(views.delete_task.as_view()), name='task-delete'),
    path('complete/', login_required(views.complete_task), name='task-complete'),
    path('reset/', login_required(views.reset), name='reset-points'),
]
