from django.urls import path
from .views import account_details, get_latest_data, display_data

urlpatterns = [
    path('api/account_details/', account_details, name='receive_json'),
    path('api/retrieve_data/', get_latest_data, name='latest_data'),
    path('display/', display_data, name='display_data'),
]
