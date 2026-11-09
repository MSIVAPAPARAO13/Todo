from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    pending_count = tasks.count()
    completed_count = completed_tasks.count()
    total_count = pending_count + completed_count
    completion_rate = int((completed_count / total_count * 100)) if total_count > 0 else 0

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'pending_count': pending_count,
        'completed_count': completed_count,
        'total_count': total_count,
        'completion_rate': completion_rate,
    }

    return render(request, 'home.html', context)
