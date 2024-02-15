from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.login, name="login"),
    path('project_list', v.project_list, name="project_list"),
    path('project_detail/<int:project_id>', v.project_detail, name="project_detail"),
    path('project_create', v.project_create, name='project_create'),
    path('project_update/<int:project_id>', v.project_update, name="project_update"),
    path('project_delete/<int:project_id>', v.project_delete, name="project_delete"),
    path('task_create/<int:project_id>', v.task_create, name='task_create'),
    path('task_update/<int:task_id>', v.task_update, name="task_update"),
    path('task_delete/<int:task_id>', v.task_delete, name="task_delete"),
]
