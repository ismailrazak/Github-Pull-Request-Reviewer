from django.urls import include, path

from .views import CheckTaskView, StartTaskView

urlpatterns = [
    path("start_task/", StartTaskView.as_view()),
    path("check_task/<str:task_id>/", CheckTaskView.as_view()),
]
