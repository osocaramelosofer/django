from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Gym


class GymView(TemplateView):
    template_name = 'gym/gym.html'


# view for list all instances of Gym table
# ListView nos entrega todas las intancias de la tabla a la que hace referencia [ ]
class ListGymView(ListView):
    model = Gym
    # gyms / object_list = Select * from Gym 
    context_object_name = 'gyms'

    template_name = 'gym/list.html'

# DetailView nos entrega una sola instancia de la tabla a la que se hace referencia 1
class GymDetailView(DetailView):
    model = Gym

    template_name = 'gym/detail_gym.html'

# View to create a new instance of Gym
class GymCreateView(CreateView):
    model = Gym
    template_name = 'gym/gym_new.html'
    fields = ['name', 'location', 'capacity']


def vue_test(request):
    return render(request, 'app.html')