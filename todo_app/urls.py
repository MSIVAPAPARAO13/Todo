from django.urls import path, include
from . import views


urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
  path('mark-as-done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # New URL for Mark as Undone
    path('mark-as-undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    #Edit Task URL
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #Delete Task URL
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')
]

