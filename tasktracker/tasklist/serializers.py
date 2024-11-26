from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TaskFilter(filters.FilterSet):
    state = CharFilterInFilter(field_name='state', lookup_expr='in')
    priority = CharFilterInFilter(field_name='priority', lookup_expr='in')
    executor = CharFilterInFilter(field_name='executor', lookup_expr='in')
    deadline = filters.DateFilter()
    time_create_gt = filters.DateFilter(field_name='time_create', lookup_expr='gte')
    time_create_lt = filters.DateFilter(field_name='time_create', lookup_expr='lte')
    time_update_gt = filters.DateFilter(field_name='time_update', lookup_expr='gte')
    time_update_lt = filters.DateFilter(field_name='time_update', lookup_expr='lte')
    title = CharFilterInFilter(lookup_expr='icontains', field_name='title')
    ordering = filters.OrderingFilter(fields=('time_create', 'time_update'))

    class Meta:
        model = Task
        fields = '__all__'


class CommentsFilter(filters.FilterSet):
    task = CharFilterInFilter(field_name='task', lookup_expr='in')

class ParticipantFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    project = CharFilterInFilter(field_name='project', lookup_expr='in')

class ProfileFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    project = CharFilterInFilter(field_name='current_project', lookup_expr='in')


class ProjectFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(fields=('time_create', 'time_update'))
    title = CharFilterInFilter(lookup_expr='in', field_name='title')

    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['task', 'comment_for_task']
        read_only_fields = ['name']
