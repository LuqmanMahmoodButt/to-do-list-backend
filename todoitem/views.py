from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# controller file 
# Create your views here.
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.exceptions import NotFound
from .models import Todoitem
from .serializers.common import TodoitemSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers.populated import PopulateTodoitemSerializer

class ItemlistView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        todoitems = Todoitem.objects.all()
        serialized_todoitems = PopulateTodoitemSerializer(todoitems, many=True)
        return Response(serialized_todoitems.data, status=status.HTTP_200_OK)
  

    def post(self, request):
  
        todoitem_to_add = TodoitemSerializer(data=request.data)
        try:
            todoitem_to_add.is_valid()
            todoitem_to_add.save()
            return Response(todoitem_to_add.data, status=status.HTTP_201_CREATED)    
        except Exception as e:
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class itemlistDetailView(APIView):
   
    def get_todoitem(self, pk):
        try:
            return Todoitem.objects.get(pk=pk)
        except Todoitem.DoesNotExist:
            raise NotFound(detail="cant find the car")

    def get(self, _request, pk):
        try:
            todoitem = self.get_todoitem(pk=pk)
            serializer_todoitem = PopulateTodoitemSerializer(todoitem)
            return Response(serializer_todoitem.data, status=status.HTTP_200_OK)
        except Todoitem.DoesNotExist:
            raise NotFound(detail="Can't find that book")
    
    def put(self, request, pk):
        todoitem_to_edit = self.get_todoitem(pk=pk)
        if todoitem_to_edit.owner.id != request.user.id and not (request.user.is_staff or request.user.is_superuser):
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
        original_user = todoitem_to_edit.owner.id  
        request.data['user'] = original_user
        updated_todoitem = TodoitemSerializer(todoitem_to_edit, data=request.data)
        
        if updated_todoitem.is_valid():
            updated_todoitem.save()
            return Response(updated_todoitem.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(updated_todoitem.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        todoitem_to_delete = self.get_todoitem(pk=pk)
        todoitem_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)