from rest_framework import serializers
from .models import AppUser, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)

class AppUserSerializer(serializers.ModelSerializer):
    Department = DepartmentSerializer(read_only=True, many=True)

    class Meta:
        model = AppUser
        fields = ('Department', 'login', 'first_name', 'last_name', 'email_addr')