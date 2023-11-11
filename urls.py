from django.urls import path , include

from utilizador import views


app_name = "utilizador"




urlpatterns = [

    # path("set_language/<str:user_language>/", views.set_language_from_url, name="set_language_from_url"),
	# path('main', views.index, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.index, name='login'),
    path('index', views.index, name='index'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('painel/', views.painel, name='painel'),


    # path('userperfil/', views.userperfil, name='userperfil')
    

]