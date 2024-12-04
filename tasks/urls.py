# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet, TaskListCreate, TaskUpdate
#
# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)
# # router.register(r'bask', TaskListCreate.as_view(), basename='bask')
#
# urlpatterns = [
#     path('tasks/', TaskListCreate.as_view(), name='venue-list-create'),
#     path('tasks/<int:id>/', TaskUpdate.as_view(), name='venue-list-create'),
#
# ]
from django.urls import path
from .views import TaskCreateAPIView, TaskListAPIView, TaskDetailAPIView, TaskUpdateAPIView, TaskDeleteAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),  # Get all tasks
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task-detail'),  # Get a specific task by ID
    path('tasks/', TaskCreateAPIView.as_view(), name='task-create'),  # Create a new task
    path('tasks/<int:id>/', TaskUpdateAPIView.as_view(), name='task-update'),  # Update a task
    path('tasks/<int:id>/', TaskDeleteAPIView.as_view(), name='task-delete'),  # Delete a task
]
