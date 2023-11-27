from django import forms
from django.forms import ModelForm
from basic.models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Enter your message', 'type':'text'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter your phone'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Enter your subject'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ('identity', 'full_name', 'contact', 'address', 'age')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['identity'].widget.attrs.update({'placeholder': 'Enter your id number'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Eneter your full name'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'Enter your company name'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Enter your address'})
        self.fields['age'].widget.attrs.update({'placeholder': 'Enter your age'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class NetworkForm2(forms.ModelForm):
    class Meta:
        model = Network
        fields =  ( 'city', 'membership', 'best_calltime', 'company_name', 'registration_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter your city', 'id': 'city_id'})
        self.fields['membership'].widget.attrs.update({'placeholder': 'Choose your membership'})
        self.fields['best_calltime'].widget.attrs.update({'placeholder': 'Enter your best call time'})
        self.fields['company_name'].widget.attrs.update({'placeholder': 'Enter your company name'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class NetworkForm3(forms.ModelForm):
    class Meta:
        model = Network
        fields =   ( 'company_address', 'business_size', 'category', 'industry', 'have_record', 'can_recieve_updates', 
        'allow_data_access')

class NetworkUpdateForm(forms.ModelForm):
    class Meta:
        model = Network
        fields =  ('user', 'identity', 'full_name', 'email', 'contact', 'address', 'city', 'membership', 'best_calltime', 'company_name', 'registration_number', 'age', 'company_address', 'business_size', 'category', 'industry', 'have_record', 'can_recieve_updates', 'allow_data_access',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter your city', 'id': 'city_id'})
        self.fields['membership'].widget.attrs.update({'placeholder': 'Choose your membership'})
        self.fields['best_calltime'].widget.attrs.update({'placeholder': 'Enter your best call time'})
        self.fields['company_name'].widget.attrs.update({'placeholder': 'Enter your company name'})
        self.fields['have_record'].widget.attrs.update({'placeholder': 'Enter your company name', })
        # 'have_record', 'can_recieve_updates', 'allow_data_access',)
        self.fields['have_record'].label = 'Do you have an criminal record?'
        self.fields['have_record'].help_text = '\n\n'
        self.fields['can_recieve_updates'].label = 'Do you grant FAN permission to utIlize your company information for marketing purposes?'
        self.fields['can_recieve_updates'].help_text = '\n\n'
        self.fields['allow_data_access'].label = 'Do you allow FAN access to your CIPC business portal for purposes of accessing supporting documents?'
        self.fields['allow_data_access'].help_text = '\n\n'
        # for field in self.fields:
        #     self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['identity'].widget.attrs.update({'placeholder': 'Enter your identity', 'id': 'identity_id'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['company_name'].widget.attrs.update({'placeholder': 'Enter your company name'})
        self.fields['registration_number'].widget.attrs.update({'placeholder': 'Enter your company registration_number', })

        
        self.fields['industry'].widget.attrs.update({'placeholder': 'Enter your industry', 'id': 'industry_id'})
        self.fields['age'].widget.attrs.update({'placeholder': 'Enter your age'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Enter your company category'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Enter your address'})
        self.fields['company_address'].widget.attrs.update({'placeholder': 'Enter your company address'})
        # self.fields['registration_number'].widget.attrs.update({'placeholder': 'Enter your company registration_number', })

        