from rest_framework.serializers import ModelSerializer

from .models import *

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"