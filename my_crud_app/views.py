from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

@csrf_exempt
def project_create(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)

        obj = Project.objects.create(
            name = name,
            description = description,
            start_date = start_date,
            end_date = end_date
        )

        project = {
            'id':obj.id,
            'name':obj.name,
            'description':obj.description,
            'start_date':obj.start_date, 
            'end_date': end_date
        }

        data = {
            'project': project,
            'project_details_url': f"project_detail/{obj.id}"
        }
        return JsonResponse(data)

@csrf_exempt
def project_delete(request):
    if request.method == "POST":
        id = request.POST.get('id', None)
        Project.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@csrf_exempt
def project_update(request):
    if request.method == "POST":
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)

        obj = Project.objects.get(id=id)
        obj.name = name
        obj.description = description
        obj.start_date = start_date
        obj.end_date = end_date
        obj.save()

        project = {
            'id':obj.id,
            'name':obj.name,
            'description':obj.description,
            'start_date':obj.start_date, 
            'end_date': end_date
        }

        data = {
            'project': project
        }
        return JsonResponse(data)
    
@csrf_exempt
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})

@csrf_exempt
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        status = request.POST.get("status")
        project_id = request.POST.get("project_id")

        obj = Task.objects.create(
            title=title, 
            description=description, 
            deadline=deadline, 
            status=status, 
            project_id=project_id)

        task = {
            'id':obj.id,
            'title':obj.title,
            'description':obj.description,
            'deadline':obj.deadline, 
            'status': obj.status,
            'project_id':obj.project_id,
        }

        data = {
            'task': task
        }
        return JsonResponse(data)

@csrf_exempt
def task_update(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        status = request.POST.get("status")

        obj = Task.objects.get(id=id)
        obj.title = title
        obj.description = description
        obj.deadline = deadline
        obj.status = status
        obj.save()

        task = {
            'id':obj.id,
            'title':obj.title,
            'description':obj.description,
            'deadline':obj.deadline,
            'status': obj.status,
            'project_id':obj.project_id,
        }

        data = {
            'task': task
        }
        return JsonResponse(data)


@csrf_exempt
def task_delete(request):
    if request.method == "POST":
        id = request.POST.get('id', None)
        Task.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)