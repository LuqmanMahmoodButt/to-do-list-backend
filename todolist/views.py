from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.exceptions import NotFound
from .serializers.populated import PopulateTodolistSerializer
from .models import Todolist
from .serializers.common import TodolistSerializer
from rest_framework.permissions import IsAuthenticated



class TodolistView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logged_in_user = request.user.id
        todolists = Todolist.objects.filter(user=logged_in_user)
        serialized_todolists = PopulateTodolistSerializer(todolists, many=True)
        return Response(serialized_todolists.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data["user"] = request.user.id
        Todolist_to_add = TodolistSerializer(data=request.data)
        try:
            if Todolist_to_add.is_valid():
                saved_todolist = Todolist_to_add.save()
                Todolist_populated = Todolist.objects.get(pk=saved_todolist.id)
                serializer_brand = PopulateTodolistSerializer(Todolist_populated)
                return Response(serializer_brand.data, status=status.HTTP_201_CREATED)
            else:
                return Response(Todolist_to_add.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error:', str(e))
            return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   
class TodolistDetailView(APIView):
    
    def get_todolist(self, pk):
        try:
            return Todolist.objects.get(pk=pk)
        except Todolist.DoesNotExist:
            raise NotFound(detail="cant find the list")

    def get(self, _request, pk):
        try:
            Todolist = self.get_todolist(pk=pk)
            serializer_brand = PopulateTodolistSerializer(Todolist)
            return Response(serializer_brand.data, status=status.HTTP_200_OK)
        except Todolist.DoesNotExist:
            raise NotFound(detail="Can't find that list")
        
    def put(self, request, pk):
        todolist_to_edit = self.get_brand(pk=pk)
        updated_todolist = TodolistSerializer(todolist_to_edit, data=request.data)
        if updated_todolist.is_valid():
            updated_todolist.save()
        return Response(updated_todolist.data, status=status.HTTP_202_ACCEPTED)
                
    def delete(self, _request, pk):
        todolist_to_delete = self.get_todolist(pk=pk)
        todolist_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
