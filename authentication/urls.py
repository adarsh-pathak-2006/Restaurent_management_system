from django.urls import path
from authentication.views import RegisterAPI
from authentication.views import CustomTokenObtain, CustomTokenRefresh

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('token/', CustomTokenObtain.as_view(), name='token_obtain_view'),
    path('token/refresh/', CustomTokenRefresh.as_view(), name='token_refresh'),
]
