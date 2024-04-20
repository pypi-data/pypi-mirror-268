import django.contrib.auth
from django.utils import timezone
from dinero_auth.crypto import  Crypt
from dinero_auth.models import DineroToken
import json
from django.contrib.auth.models import User
from rest_framework.authentication import  get_authorization_header

class AuthToken:
    
    def __init__(self,request) -> None:
        
        self.__request = request
        
    def create_token(self,data):
        strToEnc = json.dumps(data)
        crypt = Crypt()
        token = crypt.encrypt(strToEnc)
        return token
        
    def get_user_ip(self) -> str:
        
        x_forwarded_for = self.__request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')
        else:
            ip = self.__request.META.get('REMOTE_ADDR')
        
        return ip
    
    def get_user_browser_info(self) -> str:
        
        return self.__request.META['HTTP_USER_AGENT']
        
    def create(self,id) -> str:
        
        ip = self.get_user_ip()
        browser = self.get_user_browser_info()
        user = User.objects.get(id = id)
        
        tkn_obj = DineroToken.objects.create(user = user ,browser = browser ,ip = ip ,)
        
        data =  {
            "id" : tkn_obj.id,
            "user" : user.id,
            "ip" : ip,
            "browser" : browser
        }
        
        token = self.create_token(data)
        tkn_obj.token = token
        tkn_obj.save()
        
        return token
    
    def get_token_information(self,token):
        plainText = Crypt().decrypt(token)
        data = json.loads(plainText)
        return data["id"]
    
    def logout(self):
        
        auth = get_authorization_header(self.__request).split()
        
        tkn_id = self.get_token_information(auth[1].decode())
        
        if DineroToken.objects.filter(id = tkn_id).exists():
            DineroToken.objects.filter(id = tkn_id).delete()