from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()


# we are going to extend the BaseException class , because is already has things like password and email validation 


class JWTAuthentication(BasicAuthentication):# assertain users permissions # requests come through here # assign a permission level # if valid token -> given permission to see secure things
    def authenticate(self, request): # check requets has token and return if so
        header = request.headers.get('Authorization')
 # if no headers, just return to end the request
        if not header:
            return None
        
        if not header.startswith('Bearer'):
            raise PermissionDenied(detail="Invalid Auth Token")
        
        token = header.replace('Bearer ', '')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            user = User.objects.get(pk=payload.get('sub'))
            print("USER -->", user)
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail="Invalid Token") 
        
        except User.DoesNotExist:
            raise PermissionDenied(detail="Invalid User")
        
        return (user, token)
