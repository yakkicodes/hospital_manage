from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('booking/',views.booking,name='booking'),
    path('department/',views.Department,name='department'),
    path('detials/',views.Detials,name='detials'),
    path('members/',views.members,name='members'),
    path('booking/', views.booking, name='booking'),
    path('booking/summary/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/confirmed/', views.booking_success, name='booking_success'),
    path('booking/edit/<int:booking_id>/',views.booking_edit,name='booking_edit')



 ]
