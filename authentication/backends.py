import jwt
from django.conf import settings
from rest_framework import authentication,exceptions
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_Data = authentication.get_authorization_header(request)

        if not auth_Data:
            return None
        
        prefix,token=auth_Data.decode('utf-8').split(' ')

        try:
            payload=jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=["HS256"])
            print(payload)

            user=User.objects.get(username=payload['username'])
            print(user)
            return (user,token)
        
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token has expired,login')
        