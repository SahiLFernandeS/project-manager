from django.contrib import admin

from my_crud_app.models import *
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass