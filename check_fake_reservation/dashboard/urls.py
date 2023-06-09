from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_admin_reservation_dashboard, name='dashboard'),
    path('profil', views.user_profil, name='profil'),
    
    #users 
    path('user', views.user_list, name='user_list'),
    path('add_user', views.add_user, name='add_user'),
    path('show_user/<str:pk>/', views.show_user, name='show_user'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user'),
    path('update_user/<str:pk>/', views.update_user, name='update_user'),

    
    #passengers 
    path('passenger', views.passenger_list, name='passenger_list'),
    path('add_passenger', views.add_passenger, name='add_passenger'),
    path('show_passenger/<str:pk>/', views.show_passenger, name='show_passenger'),
    path('delete_passenger/<str:pk>/', views.delete_passenger, name='delete_passenger'),
    path('update_passenger/<str:pk>/', views.update_passenger, name='update_passenger'),


    #flights      
    path('flights', views.flights_list, name='flight_list'),
    path('add_flight', views.add_flight, name='add_flight'),
    path('show_flight/<str:pk>/', views.show_flight, name='show_flight'),
    path('delete_flight/<str:pk>/', views.delete_flight, name='delete_flight'),
    path('update_flight/<str:pk>/', views.update_flight, name='update_flight'),

    
    #flights available
    path('flights_available', views.flights_available_list, name='flights_available_list'),
    path('flights_available_view/<str:pk>/', views.flights_available_view, name='flights_available_view'),
    
    #Reservation available
    path('reservations', views.reservation_list, name='reservation_list'),
    path('show_reservation/<str:pk>/', views.show_reservation, name='show_reservation'),
    path('delete_reservation/<str:pk>/', views.delete_reservation, name='delete_reservation'),
    path('make_reservation_true/<str:pk>/', views.make_reservation_true, name='make_reservation_true'),

    #My reservation
    path('my_reservation_list', views.my_reservation_list, name='my_reservation_list'),
    path('show_my_reservation/<str:pk>', views.show_my_reservation, name='show_my_reservation'),
    path('delete_my_reservation/<str:pk>', views.delete_my_reservation, name='delete_my_reservation'),


    #prediction
    path('predict_reservations', views.predict_reservation_list, name='predict_reservations_list'),
    path('predict_reservation_reset_all', views.predict_reservation_reset_all, name='predict_reservation_reset_all'),
    path('predict_reservation_show/<str:pk>', views.predict_reservation_show, name='predict_reservation_show'),
    path('predict_reservation', views.predict_reservation, name='predict_reservation'),
    path('export_csv', views.export_csv, name='export_csv'),




]


   