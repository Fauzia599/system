from rest_framework import serializers
from .models import *

class CleanerSerializar(serializers.ModelSerializer):
    class  Meta:
        model = Cleaner
        fields = "__all__"

class TaskSerializar(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        

class FacilitySerializar(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
        