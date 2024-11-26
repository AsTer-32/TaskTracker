from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', blank=True, default='media/img/anonym.png')
    role = models.CharField(max_length=50, default=None)
    current_project = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=20, choices=[('active', 'active'), ('archived', 'archived')], default='new')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    executor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="executor")  # исполнитель
    state = models.CharField(max_length=20, choices=[('Grooming', 'Grooming'),  ('In Progress', 'In Progress'), ('Dev', 'Dev'), ('Done', 'Done')], default='new')
    priority = models.CharField(max_length=20, choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='None')
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    deadline = models.DateField()
    responsible_for_testing = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tester")

    def __str__(self):
        return self.title


class Participants(models.Model): # Участник
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment_for_task = models.TextField()

