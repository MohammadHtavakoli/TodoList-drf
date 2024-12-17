from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListCreate, TaskUpdate

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='venue-list-create'),
    path('tasks/<int:id>/', TaskUpdate.as_view(), name='venue-list-create'),

]



