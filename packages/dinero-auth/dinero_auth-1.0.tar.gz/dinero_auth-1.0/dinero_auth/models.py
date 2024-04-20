from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class DineroTokenManager(models.Manager):
    
    def create(self,user ,browser , ip):
        access_TTL = settings.ACCESS_TOKEN_TTL

        if access_TTL is not None:
            access_expiry = timezone.now() + access_TTL

        instance = super(DineroTokenManager, self).create(
            access_expiry = access_expiry,
            user = user,
            browser = browser,
            ip = ip
            )
        return instance


class DineroToken(models.Model):
    
    objects = DineroTokenManager()
    
    token = models.CharField( max_length=500 , null=True, blank=True )

    user = models.ForeignKey(User, null=False, blank=False, related_name='auth_token', on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    
    access_expiry = models.DateTimeField(null=True, blank=True)
    
    ip = models.CharField( max_length=500 )
    
    browser = models.CharField( max_length=500 )

    def __str__(self):
        return '%s : %s' % (self.id, self.user)
    
    class Meta:
        db_table = 'dn_token'
