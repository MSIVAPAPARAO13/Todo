from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

# Mark a completed task as undone
def mark_as_undone(request, pk):

    # Get the task using its primary key
    task = get_object_or_404(Task, pk=pk)

    # Change the task status to False
    task.is_completed = False

    # Save the changes in the database
    task.save()

    # Redirect to the home page
    return redirect('/')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')

    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')