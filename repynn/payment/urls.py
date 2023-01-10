from django.urls import path
from . import views

app_name = 'payment'


urlpatterns = [
    path('process/', views.payment_process, name='process'),  # the order summary 
    path('completed/', views.payment_completed, name='completed'),  # successful
    path('canceled/', views.payment_canceled, name='canceled'),  # canceled
]
