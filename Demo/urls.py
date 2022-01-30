from django.urls import path
from .views import ServicesList


app_name = 'Demo'

urlpatterns = [
    path('', ServicesList.as_view(), name='services_list'),

]
