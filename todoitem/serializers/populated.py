from .common import TodoitemSerializer
from todolist.serializers.common import ToDoListSerializer

class PopulateCarSerializer(TodoitemSerializer):
    todolist = ToDoListSerializer()