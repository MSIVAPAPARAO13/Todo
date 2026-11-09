from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Task

def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task', '').strip()
        if task_text:
            Task.objects.create(task=task_text)
            messages.success(request, 'Task added successfully!')
        else:
            messages.warning(request, 'Task title cannot be empty!')
        return redirect('home')
    return render(request, 'addTask.html')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    messages.success(request, f'Task completed: "{task.task}"')
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    messages.info(request, f'Task marked as pending: "{task.task}"')
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task_text = request.POST.get('task', '').strip()
        if task_text:
            task.task = task_text
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('home')
        else:
            messages.warning(request, 'Task title cannot be empty!')

    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_name = task.task
    task.delete()
    messages.success(request, f'Task deleted: "{task_name}"')
    return redirect('home')
