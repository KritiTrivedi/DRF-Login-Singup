# urls.py
from django.urls import path
from . import views

urlpatterns = [
#     path('register/', views.registration.as_view(), name='register'),
  path('register',views.register,name="register"),


    path('LoginApi',views.Login,name="LoginApi"),
]
