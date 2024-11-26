from typing import Required

from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


# ПАГИНАЦИЯ
class APIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


# ЗАДАЧИ
class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = APIListPagination
    filterset_class = TaskFilter
    filter_backends = [DjangoFilterBackend]


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAdminOrReadOnly, )


# ПРОЕКТЫ
class ProjectAPIList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = APIListPagination
    filterset_class = ProjectFilter
    filter_backends = [DjangoFilterBackend]


class ProjectAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ProjectAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (IsAdminOrReadOnly, )


# ПРОФИЛЬ
class ProfileAPIList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    filterset_class = ProfileFilter
    filter_backends = [DjangoFilterBackend]


class ProfileAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ProfileAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAdminOrReadOnly, )


# УЧАСТНИКИ
class ParticipantsAPIList(generics.ListCreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = APIListPagination
    filterset_class = ParticipantFilter
    filter_backends = [DjangoFilterBackend]


class ParticipantsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ParticipantsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


# COMMENTS
class CommentsAPIList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = (IsAuthenticated, )
    pagination_class = APIListPagination
    filterset_class = CommentsFilter
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)


class CommentsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class CommentsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )

def send_notification_email(requests, email):
    subject = 'Уведомление'
    message = f'Тебя добавили в проект'
    from_email = 'artur.gafurov2008@yandex.ru'
    recipient_list = email
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Уведомление отправлено')


