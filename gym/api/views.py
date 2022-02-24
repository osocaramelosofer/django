import json

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


from ..models import Gym
from .serializers import GymSerializer

# Dave way(functions)
def list_gyms(request):
    # request_data = json.loads(request.body)
    query = Gym.objects.all()
    
    # NOTE: if the query returns many instances we need to add many=True
    serialized_data = GymSerializer(query, many=True).data

    response = {
        'data': serialized_data
    }

    return JsonResponse(response)

# when you use APIView you hace to include in the urls like thi: gym_api_views.ListGymsAPIView.as_view()
class ListGymsAPIView(APIView):

    def get(self, request, format=None):
        gyms = [gym.name for gym in Gym.objects.all()]
        
        return Response(gyms)


# gym_api_views.List2.as_view()
class List2(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
