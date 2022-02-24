from django.urls import path
from .views import GymView, ListGymView, GymDetailView, GymCreateView, vue_test
from .api import views as gym_api_views
# Gym urls
urlpatterns = [
    path('gym/new/', GymCreateView.as_view(), name="gym_new"),
    path('<int:pk>/', GymDetailView.as_view(), name="gym_detail"),
    path('home/',GymView.as_view(), name="gym_view"),
    path('', ListGymView.as_view(), name='list_gym'),
    path('vue-test', vue_test),
    path('gym_api_views', gym_api_views.ListGymsAPIView.as_view(), name="gym-api-view"),
    path('list_gym_def', gym_api_views.list_gyms, name="list-gym-def")


]