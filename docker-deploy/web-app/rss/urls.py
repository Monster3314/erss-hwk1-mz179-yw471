"""rss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from driver import views as driver_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
    path('register/',user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('update_profile/',user_views.update_profile,name='update_profile'),
    path('driver/', user_views.driver, name='driver'),
    path('driver_register/', driver_views.driver_register, name='driver_register'),
    path('search/', driver_views.search, name='search'),
    path('request_ride/', user_views.request_ride, name='request_ride'),
    path('details/<int:ride_id>', user_views.ride_details, name='details'),
    path('edit_ride/<int:ride_id>', user_views.edit_ride, name='edit_ride'),
    path('search_ride/', user_views.search_ride, name='search_ride'),
    path('join_ride/<int:ride_id>', user_views.join_ride, name='join_ride'),
    path('cancel_ride/<int:ride_id>', user_views.cancel_ride, name='cancel_ride'),
    path('complete_ride/<int:ride_id>', user_views.complete_ride, name='complete_ride'),
    path('edit_ride/<int:ride_id>', user_views.edit_ride, name='edit_ride'),
    path('confirm_ride/<int:ride_id>', user_views.confirm_ride, name='confirm_ride'),
    path('leave_ride/<int:ride_id>', user_views.leave_ride, name='leave_ride'),
    path('driver_search/', user_views.driver_search, name='driver_search'),
    path('driver_details/<int:ride_id>', user_views.driver_details, name='driver_details'),
    # path('search_result/', user_views.search_result, name='search_result'),
]