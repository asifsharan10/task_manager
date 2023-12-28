from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(View):
    template_name = 'tasks/task_list.html'

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, self.template_name, {'tasks': tasks})

class TaskCreateView(View):
    template_name = 'tasks/task_form.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})

class TaskDetailView(View):
    template_name = 'tasks/task_detail.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        return render(request, self.template_name, {'task': task})

class TaskUpdateView(View):
    template_name = 'tasks/task_form.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, self.template_name, {'form': form})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})

class TaskDeleteView(View):
    template_name = 'tasks/task_confirm_delete.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        return render(request, self.template_name, {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        return redirect('task_list')


              
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
