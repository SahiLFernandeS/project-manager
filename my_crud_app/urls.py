from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.projects, name='project_list'),
    path('project_create', v.project_create, name='project_create'),
    path('project_delete', v.project_delete, name='project_delete'),
    path('project_update', v.project_update, name='project_update'),
    path('project_detail/<int:project_id>', v.project_detail, name='project_detail'),
    path('task_create', v.task_create, name='task_create'),
    path('task_update', v.task_update, name='task_update'),
    path('task_delete', v.task_delete, name='task_delete'),
]