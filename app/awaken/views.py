import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Task, Points
from .jobs import reset_points
from .util.datahelper import update_data

def view_tasks(request):
    reset_points(request.user)
    task_list = []
    try:
        task_list = Task.objects.filter(user_id = request.user)
    except:
        pass
    points = Points.objects.get(user_id=request.user).daily_points
    return render(request, 'awaken/task_list.html', {'task_list': task_list, 'points': points})

class create_task(CreateView):
    model = Task
    fields = ['title', 'points']
    def form_valid(self, form):
        user = self.request.user
        form.instance.user_id = user
        return super(create_task, self).form_valid(form)
    def get_context_data(self):
        context = super(create_task, self).get_context_data()
        context['title'] = 'Create a new item'
        return context
    def get_success_url(self):
        return reverse_lazy('index')

class edit_task(UpdateView):
    model = Task
    fields = ['title', 'points']
    def get_context_data(self):
        context = super(edit_task, self).get_context_data()
        context['title'] = 'Edit item'
        return context
    def get_success_url(self):
        return reverse_lazy('index')
    
class delete_task(DeleteView):
    model = Task
    def get_success_url(self):
        return reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

def complete_task(request):
    if request.method == 'POST':
        # maybe put getlist in a separate variable and check
        # if len == 0, might be faster
        points = sum(map(int, request.POST.getlist('task')))
        if points != 0:
            obj = Points.objects.get(user_id=request.user)
            update_data(obj, points)

    return redirect('index')

# full manual reset, for testing
def reset(request):
    obj = Points.objects.get(user_id=request.user)
    obj.daily_points = 0
    obj.weekly_points = 0
    obj.data_points = "0,0,0,0,0,0,0,0,0,0,0,0,0,0"
    obj.last_reset = datetime.date.today()
    obj.save()
    return redirect('index')
