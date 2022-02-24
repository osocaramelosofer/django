from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Coach

# Create your views here.
class ListCoach(ListView):
    model = Coach
    template_name = 'coach/coach.html'
    context_object_name = 'coach_list'