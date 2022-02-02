from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Ride, Sharer


def home(request):
    sharer = Sharer.objects.filter(sharer=request.user.username)
    rides = []
    for r in sharer:
        qs = Ride.objects.filter(id=r.ride_id, status__lt=2)
        if qs:
            rides.append(qs[0])
    context={
        'my_ride': Ride.objects.filter(owner=request.user.username, status__lt=2),
        # 'join_ride' : Ride.object.filter()
        'join_ride': rides
    }
    return render(request,'mysite/home.html',context)