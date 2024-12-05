from django.urls import path # type: ignore
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task_list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(),name='task-detail')
]
