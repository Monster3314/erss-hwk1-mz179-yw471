from django import forms
from users.models import Profile

# 与form建立关系

class driveruser(forms.ModelForm):
    class Meta:
    # models 里面建的driveruserform
        model = Profile
     # 在html里面显示的字段
     #    fields = '__all__'
        exclude = ('username',)

    # def __init__(self, *args, **kwargs):
    #     super(driveruser, self).__init__(*args, **kwargs)
    #     self.fields['username'].required = False
class update_profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('username',)


