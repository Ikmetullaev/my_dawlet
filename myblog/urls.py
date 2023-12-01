from django.urls import path
from . import views
app_name = 'myblog'

urlpatterns = [
    path('',views.homepage, name='home'),
    path('register/', views.registration, name='register'),
    path('about/', views.aboutpage, name='about'),
    path('login/', views.loginpage, name='login'),
    path('services/', views.servicespage, name='services'),
    path('services/<int:pk>/', views.servicesDetail, name='about_detail'),
    path('dawlet_add/', views.dawlet_add, name='dawlet_add'),
    path('logins/', views.loginspage, name='Logins'),
    path('menu/', views.menu, name='menu'),
    path('menu/category/<str:slug>', views.menu, name ='category'),
    path('dawlets/', views.dawlet_list, name = 'dawlets'),
    path('update/<slug:product_id>/', views.dawlet_update, name = 'update'),
]