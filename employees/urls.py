
from django.urls import path

from .api.views import EmployeeViewSet

urlpatterns = [
    path('list', EmployeeViewSet.as_view()),
]

