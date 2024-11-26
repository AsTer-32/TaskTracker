from django.contrib import admin

from .models import Project, Task, Participants, Profile, Comments

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Participants)
admin.site.register(Profile)
admin.site.register(Comments)