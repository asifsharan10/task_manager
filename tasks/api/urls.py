from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskDeleteAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='api_task_list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='api_task_detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='api_task_create'),  # Add this line for creating tasks
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='api_task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='api_task_delete'),
]
