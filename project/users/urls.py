from django.urls import path
from .import views
from .views import register_view

app_name = 'users'


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('',views.homepage, name='homepage' ),
    path('success/',views.success,name='success'),
    path('loginsuccess/',views.loginsuccess,name='loginsuccess'),
]