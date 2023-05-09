from django.urls import path

from tasks.views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('<int:pk>', TaskDetail.as_view(), name='task_detail'),
]