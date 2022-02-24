from rest_framework import serializers
from ..models import Program, ProgramRequirement

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields =['name', 'owner_name', 'telephone']

class ProgramRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramRequirement
        fields = ['name', 'type', 'program']

