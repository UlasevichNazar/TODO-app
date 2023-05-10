from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from tasks.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')
