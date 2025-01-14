from django.urls import path,include
from .views import EntryView


urlpatterns = [
    path('entry_view/',EntryView.as_view()),
]