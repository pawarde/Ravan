from django.urls import path
from . import views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_view





urlpatterns = [
    path('',views.login_page,name='Home'),
    #path('/accounts', views.uses, name="users"),
    path('users/', views.users, name='users.html'),
    path('users/users.html', views.users, name='users.html'),
    path('users/machines.html', views.MachineVision, name='machines.html'),
    path('users/report.html', views.IP_Camera, name='report.html'),
    path('users/image_tagging.html', views.Downloads, name='image_tagging.html'),
    path('users/machines/add_machine',views.add_machine,name="add_machine"),
    path('',views.logot,name="logout")

    

    # path('login/',views.login_page)

    # path('/accounts',views.home, name="Login Page")
    # # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    # path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]