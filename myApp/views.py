from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.db.models import Q


def login(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            employee = Employee.objects.filter(Q(username=username) | Q(email=email))

            if not employee:
                print("hello")
                return render(request, "login.html", {"errorMessage": "Invalid username/email or password"})
            
            if password != employee[0].password:
                print("hell2o")
                return render(request, "login.html", {"errorMessage": "Invalid username/email or password"})
            
            return redirect("project_list")
        return render(request, "login.html")
    except Exception as e:
        pass

def project_list(request):
    try:
        projects = Project.objects.all()
        return render(request, 'project_list.html', {'projects': projects})
    except Exception as e:
        print("project_list Error: ", e)
        return redirect("/")
    

def project_detail(request, project_id):
    try:
        project = get_object_or_404(Project, pk=project_id)
        tasks = Task.objects.filter(project=project)
        return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})
    except Exception as e:
        print("project_detail Error: ", e)
        return redirect("/")
    

def project_create(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            description = request.POST.get("description")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")

            project = Project(name=name, description=description, start_date=start_date, end_date=end_date)
            project.save()

            return redirect("project_list")
        return render(request, 'project_form.html')
    except Exception as e:
        print("project_create Error: ", e)
        return redirect("/")

def project_update(request, project_id):
    try:
        project = get_object_or_404(Project, pk=project_id)
        if request.method == 'POST':
            name = request.POST.get("name")
            description = request.POST.get("description")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")

            Project.objects.filter(id=project_id).update(name=name, 
                                                         description=description, 
                                                         start_date=start_date, 
                                                         end_date=end_date)
            return redirect(f"/project_list")
        return render(request, 'update_project.html', {"project": project})
    except Exception as e:
        print("project_update Error: ", e)
        return redirect("/")


def project_delete(request, project_id):
    try:
        project = get_object_or_404(Project, pk=project_id)
        if request.method == 'POST':
            project.delete()
            return redirect('project_list')
        return render(request, 'project_delete.html', {'project': project})
    except Exception as e:
        print("project_delete Error: ", e)
        return redirect("/")


def task_create(request, project_id):
    try:
        if request.method == 'POST':
            title = request.POST.get("title")
            description = request.POST.get("description")
            deadline = request.POST.get("deadline")
            status = request.POST.get("status")

            task = Task(title=title, description=description, deadline=deadline, status=status, project_id=project_id)
            task.save()
            return redirect(f"/project_detail/{project_id}")
        return render(request, 'task_form.html')
    except Exception as e:
        print("task_create Error: ", e)
        return redirect("/")


def task_update(request, task_id):
    try:
        task = get_object_or_404(Task, pk=task_id)
        if request.method == 'POST':
            title = request.POST.get("title")
            description = request.POST.get("description")
            deadline = request.POST.get("deadline")
            status = request.POST.get("status")

            Task.objects.filter(id=task_id).update(title=title, description=description, deadline=deadline, status=status)
            return redirect(f"/project_detail/{task.project_id}")
        return render(request, 'update_task.html', {'task': task})
    except Exception as e:
        print("task_update Error: ", e)
        return redirect("/")


def task_delete(request, task_id):
    try:
        task = get_object_or_404(Task, pk=task_id)
        if request.method == 'POST':
            task.delete()
            return redirect('project_detail', project_id=task.project_id)
        return render(request, 'task_delete.html', {'task': task})
    except Exception as e:
        print("task_delete Error: ", e)
        return redirect("/")