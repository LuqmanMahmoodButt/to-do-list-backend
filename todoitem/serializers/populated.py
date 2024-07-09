from .common import TodoitemSerializer
from todolist.serializers.common import TodolistSerializer

class PopulateTodoitemSerializer(TodoitemSerializer):
    todolist = TodolistSerializer()