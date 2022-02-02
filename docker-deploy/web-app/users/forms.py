# 在form里添加一个field(email)， 再写一个form继承原来的form

from django.utils import timezone

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from mysite.models import Ride

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class RideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['party', 'destination', 'arrival_time', 'to_join', 'special_info', 'vehicle_type']

    # def __init__(self, *args, **kwargs):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #     super().__init__()
    #     self.fields['special_info'].required = False
    #     self.fields['vehicle_type'].required = False

class SearchRideForm(forms.Form):
    destination = forms.CharField()
    earliest_arrival_time = forms.DateTimeField()
    latest_arrival_time = forms.DateTimeField()
    party = forms.IntegerField()


class PartyConfirmForm(forms.Form):
    party = forms.IntegerField()


