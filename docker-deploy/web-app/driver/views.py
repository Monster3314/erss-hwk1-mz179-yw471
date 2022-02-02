from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import driveruser
from users.models import Profile
from django.db import models

def driver_register(request):
    # drivername =data.get("drivername")
    # vehicle_type_registered = data.get('vehicle_type_register')
    # license_plate_number = data.get('license_plate_number')
    # capacity_of_the_car = data.get('capacity_of_the_car')
    username = request.user.username
    try:
        instance = Profile.objects.get(username=username)
        return render(request, 'users/driver.html', {'form': instance})
    except:
        if request.method == 'POST':
            form = driveruser(request.POST)
            # form.cleaned_data['username'] = username
            # form.save()
            # return render(request, 'users/driver.html', {'form': form.cleaned_data})
            if form.is_valid():
                # return Http404("test")
                instance = form.save(commit=False)
                instance.username = username
                instance.save()
                # username = form.cleaned_data.get('username')
                messages.success(request, f'account creat successful, you are a driver now')
                return render(request, 'users/driver.html', {'profile':instance})
            else:
                form = driveruser()
                return render(request,'users/driver_register.html',{'form':form})
        form = driveruser()
        return render(request, 'users/driver_register.html', {'form': form})









def search(request):
    # 从网页获得文本信息
    search_word = request.GET.get('wd','')
    # 全部匹配
    search_name= Profile.filter(user=search_word)
    context={}
    context['search_word'] = search_word
    context['search_name'] = search_name
    return render(request,'users/search.html',context)



