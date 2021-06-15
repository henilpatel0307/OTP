from django.urls import path

# from . import views as v
from .views import *

urlpatterns = [
    path('',Company_login,name='c_login'),
    path('Registration/',Company_regi,name='c_regi'),
    path('CompForgetPass/',CompForgetPass,name='CompForgetPass'),
    # path('OTP_check/',OTP_check,name='OTP_check'),
    path('DashBoard/',ComDashBoard,name='ComDashBoard'),
]
