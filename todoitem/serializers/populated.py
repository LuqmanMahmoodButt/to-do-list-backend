from .common import TodoitemSerializer
from todolist.serializers.common import ToDoListSerializer

class PopulateTodoitemSerializer(TodoitemSerializer):
    todolist = ToDoListSerializer()