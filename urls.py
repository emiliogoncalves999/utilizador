from django.urls import path , include

from utilizador import views


app_name = "utilizador"




urlpatterns = [

    # path("set_language/<str:user_language>/", views.set_language_from_url, name="set_language_from_url"),
	# path('main', views.index, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.index, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('painel/', views.painel, name='painel'),

    # path('userperfil/', views.userperfil, name='userperfil')
    

]