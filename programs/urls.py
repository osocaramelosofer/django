from django.urls import path
from .api import views as api_views

urlpatterns = [
    path('list-program', api_views.list_programs),
]