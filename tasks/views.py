from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()  
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def update_task(request):
    # Get task_id from either GET or POST parameters
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
    else:
        task_id = request.GET.get('id')
    
    # Print the task_id for debugging
    print(f"Looking for task with ID: {task_id}")
    
    # Use get_object_or_404 to handle missing tasks
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task}
    
    print('Form', form)
    
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    # Get the task or return 404 if not found
    task = get_object_or_404(Task, id=pk)
    
    # If POST request, delete the task
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    # If it's a GET request, we shouldn't reach here as we're using the modal for confirmation
    return redirect('/')