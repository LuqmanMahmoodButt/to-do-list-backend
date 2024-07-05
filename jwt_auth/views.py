from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.exceptions import PermissionDenied
from .serializers import UserSerializer
from datetime import datetime, timedelta 
from django.contrib.auth import get_user_model
from django.conf import settings 

import jwt


User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
    
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': 'User created succssfully'}, status=status.HTTP_201_CREATED)
        
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class LoginView(APIView):

    def post(self, request):
        # get the data you need out ogf the request object (email and password)
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied(detail='Invalid Details')
        
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail='Invalid Details')
        

        dt = datetime.now() + timedelta(days=7)
        
        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(dt.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({'token': token, 'message': f"Welcome Back {user_to_login.username}"})