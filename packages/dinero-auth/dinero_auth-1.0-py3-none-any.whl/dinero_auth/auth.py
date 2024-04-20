from django.conf import settings
import django.db
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header,
)
from django.utils import timezone
from dinero_auth.crypto import  Crypt
from dinero_auth.models import DineroToken
from django.contrib.auth.models import User
import json


class DineroTokenAuthentication(BaseAuthentication):
    
    def authenticate(self,request):
        auth = get_authorization_header(request).split()
        prefix = settings.AUTH_HEADER_PREFIX.encode()

        if not auth:
            return None
        
        if auth[0].lower() != prefix.lower():
            # Authorization header is possibly for another backends
            return None
        
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)
        user , auth_token = self.authenticate_credentials(request,auth[1].decode())
        return(user, auth_token)

    def authenticate_credentials(self,request, token):

        plainText = Crypt().decrypt(token)
        data = json.loads(plainText)
        valid,id = self.validate_data(request,data)
        
        if valid:
            auth_token = DineroToken.objects.get(id = id)
            current_access_expiry = auth_token.access_expiry
            
            if self.validate_user(auth_token.user):
                if current_access_expiry >= timezone.now():
                    self.refresh_token(auth_token)
                    
                else:
                    msg = 'The authentication token provided is expired. Please Relogin!'
                    raise exceptions.AuthenticationFailed(msg)
                return auth_token.user,auth_token.token
        else:
            msg = 'The authentication token provided is invalid or corrupt.'
            raise exceptions.AuthenticationFailed(msg)
        
    def refresh_token(self,auth_token):
        return True
        
    
    def validate_user(self,user):
        if not user.is_active:
                    raise exceptions.AuthenticationFailed('User inactive or deleted.')
        return True
            
    def validate_data(self,request,data):
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            crnt_ip = x_forwarded_for.split(',')[0]
        else:
            crnt_ip = request.META.get('REMOTE_ADDR')
        
        crnt_browser = request.META['HTTP_USER_AGENT']
        if DineroToken.objects.filter(id = data["id"]).exists():
            tkn = DineroToken.objects.get(id = data["id"])
            
            v_browser = crnt_browser == data["browser"] == tkn.browser
            v_ip = crnt_ip == data["ip"] == tkn.ip
            v_user = data["user"] == tkn.user.id
        
            if any(not value for value in [v_ip,v_browser,v_user]):
                msg = 'The authentication token provided is invalid or corrupt.'
                raise exceptions.AuthenticationFailed(msg)

            return True,data["id"]
        return False,None