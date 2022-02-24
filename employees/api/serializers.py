from rest_framework import serializers
from ..models import Employee, File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['name', 'employee']


class EmployeeSerializer(serializers.ModelSerializer):
    contract = FileSerializer()
    rfc = FileSerializer()

    class Meta:
        model = Employee
        fields = ['name', 'contract', 'rfc']

    def create(self, validated_data):
        # validated_data nos regresa un directory { }

        contract = validated_data.pop('contract')
        rfc = validated_data.pop('rfc')

        employee_instance = Employee.objects.create(**validated_data)

        contract_instance = File.objects.create(name=contract['name'], employee=employee_instance)
        employee_instance.contract = contract_instance

        return employee_instance


