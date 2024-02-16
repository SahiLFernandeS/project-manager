from django.db import models


class Employee(models.Model):

    ROLE_CHOICES = [ 
        ('Admin', 'Admin'), 
        ('Employee', 'Employee'),
        ('Manager', 'Manager')
        ]

    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Employee'

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Project'
    
    

class Task(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Task'
