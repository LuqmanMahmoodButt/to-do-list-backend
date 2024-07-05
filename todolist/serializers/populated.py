from .common import TodolistSerializer
from todoitem.serializers.common import TodoitemSerializer

class PopulateTodolistSerializer(TodolistSerializer):
    items = TodoitemSerializer(many=True)