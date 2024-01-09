from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view()),
    path('logout', views.Logout),
]



doctor_urls = [
    path('doctor/register', views.DoctorRegister.as_view()),
    path('doctor/dashboard', views.DoctorDashboard.as_view(), name='doctor_dashboard'),
]

user_urls = [
    path('user/register', views.UserRegister.as_view()),
    path('user/dashboard', views.UserDashboard.as_view(), name="user_dashboard"),
]


urlpatterns += user_urls
urlpatterns += doctor_urls