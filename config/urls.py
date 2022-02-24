from django.contrib import admin

from django.urls import path, include # new

# global urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
    path('coach/', include('coach.urls')), # coach urls
    path('gym/', include('gym.urls')),
    path('api/', include('employees.urls')),
    path('program/', include('programs.urls')),
    path('publications/', include('publications.urls'))
]