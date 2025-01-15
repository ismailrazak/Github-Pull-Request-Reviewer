from django.urls import path,include
from .views import StartTaskView,CheckTaskView


urlpatterns = [
    path('start_task/',StartTaskView.as_view()),
    path('check_task/<str:task_id>/',CheckTaskView.as_view()),
]