# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home_page, name='home_page'),

    path('modelo/', views.modelo_page, name='modelo_page'),
    
 
    path('cadastros/', views.cadastro_usuario, name='cadastro_usuario'),
    

    path('login/', views.login_usuario, name='login_page'),
    path('logout/', views.user_logout, name='logout'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
]