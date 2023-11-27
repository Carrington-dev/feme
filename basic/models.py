from django.db import models
from basic.variables import *

from webapp import settings


class Contact(models.Model):
    """Model definition for Contact."""
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    date_recieved		    = models.DateTimeField(verbose_name='date recieved', auto_now_add=True)
    date_last_viewed		= models.DateTimeField(verbose_name='last viewed', auto_now=True)


    class Meta:
        """Meta definition for Contact."""
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return f"{self.name} {self.subject}"

class Subscribe(models.Model):
    email                   = models.EmailField(max_length=200, verbose_name='email', unique=True)
    is_subscribed           = models.BooleanField(default=True ,verbose_name='subscribed' )
    date_recieved		    = models.DateTimeField(verbose_name='date recieved', auto_now_add=True)
    date_last_viewed		= models.DateTimeField(verbose_name='last viewed', auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'


class Network(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    identity = models.CharField(max_length=200, help_text='9708098714087')
    full_name = models.CharField(max_length=300, verbose_name='Enter your full name')
    email = models.EmailField(max_length=30)
    contact = models.CharField(max_length=20, help_text='012 270 2333')
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    membership = models.CharField(max_length=200, choices=MEMBERSHIP, default = 'Job/Learnship Seeker')
    best_calltime = models.CharField(max_length=200, choices=BEST_TIME, default = 'Morning')
    company_name = models.CharField(max_length=300, blank=True, null=True,  verbose_name='Enter your company name')
    registration_number = models.CharField(max_length=60, blank=True, null=True)
    age = models.IntegerField(help_text='Your age')
    company_address = models.CharField(max_length=200, blank=True, null=True)
    business_size = models.CharField(max_length=200, choices=BUSINESS_SIZE, default = 'Small')
    category = models.CharField(max_length=200,  null=True, blank=True) #"""choices=BUSINESS_CATEGORY,"""
    industry = models.CharField(max_length=200, null=True, blank=True)
    have_record = models.BooleanField(default=False, help_text='Do you have a criminal record?') 
    can_recieve_updates = models.BooleanField(default=True, help_text='Do you grant FAN permission to utIlize your company information for marketing purposes?') 
    allow_data_access = models.BooleanField(default=True, help_text='Do you allow FAN access to your CIPC business portal for purposes of accessing supporting documents?') 
    date_applied = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.identity

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'

    