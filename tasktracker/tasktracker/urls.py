from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from tasklist.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task Tracker",
      default_version='v1',
   )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/tasklist/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/v1/projectlist/', ProjectAPIList.as_view()),
    path('api/v1/project/<int:pk>/', ProjectAPIUpdate.as_view()),
    path('api/v1/projectdelete/<int:pk>/', ProjectAPIDestroy.as_view()),
    path('api/v1/profilecreate/', ProfileAPIList.as_view()),
    path('api/v1/profile/<int:pk>/', ProfileAPIUpdate.as_view()),
    path('api/v1/profiledelete/<int:pk>/', ProfileAPIDestroy.as_view()),
    path('api/v1/participantlist/', ParticipantsAPIList.as_view()),
    path('api/v1/participant/<int:pk>/', ParticipantsAPIUpdate.as_view()),
    path('api/v1/participantdelete/<int:pk>/', ParticipantsAPIDestroy.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/commentlist/', CommentsAPIList.as_view()),
    path('api/v1/comment/<int:pk>/', CommentsAPIUpdate.as_view()),
    path('api/v1/commentdelete/<int:pk>/', CommentsAPIDestroy.as_view()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
]
