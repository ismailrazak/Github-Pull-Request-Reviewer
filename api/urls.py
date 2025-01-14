from django.urls import path,include
from .views import StartTaskView


urlpatterns = [
    path('start_task/',StartTaskView.as_view()),
]