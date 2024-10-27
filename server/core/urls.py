from django.urls import path, include
from .views import (
    TaskListView,
    TaskCreateView,
    TaskEditView,
    TaskCancelView,
    TaskCompleteView,
    TaskDeleteView,
)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/jwt/', include('djoser.urls.jwt')),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/edit/<int:id>/', TaskEditView.as_view(), name='task-edit'),
    path('tasks/cancel/<int:id>/', TaskCancelView.as_view(), name='task-cancel'),
    path('tasks/complete/<int:id>/', TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/delete/<int:id>/', TaskDeleteView.as_view(), name='task-delete'),
]