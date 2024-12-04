# from rest_framework import viewsets,generics
# from .models import Task
# from .serializers import TaskSerializer
#
# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-created_at')
#     serializer_class = TaskSerializer
#
# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     def perform_create(self, serializer):
#         # You can add custom logic here if needed
#         serializer.save()
#
#
# class TaskUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     lookup_field = 'id'
#


from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
