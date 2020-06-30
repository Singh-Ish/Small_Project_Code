from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms',views.form_name_view, name='form_name'),
    path('users', views.users, name ='user_form')
]
