from rest_framework import serializers
from ..models import Todoitem


class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = '__all__'