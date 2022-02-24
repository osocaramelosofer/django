from django.urls import path
from .views import ListCoach

# Coach urls
urlpatterns = [
    path('list', ListCoach.as_view(), name='list_coach'),
]