import json
from django.http import JsonResponse

from .serializers import ProgramSerializer
from ..models import Program


def list_programs(request):
    query = Program.objects.all()
    # print('$$$$ ',ProgramSerializer(query))
    serialized_data = ProgramSerializer(query, many=True).data

    return JsonResponse({'hola': serialized_data})