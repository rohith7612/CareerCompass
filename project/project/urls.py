"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='homepage' ),
    path('roadmaps/',views.roadmaps_view, name='roadmaps'),
    path('companies/',views.companies,name='companies'),
    
    
    path('frontend/',views.frontend,name='frontend'),
    path('DevOps/',views.DevOps,name = 'DevOps'),
    path('Ai/',views.Ai,name = 'Ai'),
    path('Cloud/',views.Cloud,name = 'Cloud'),
    path('cybersecurity/',views.cybersecurity,name = 'cybersecurity'),
    path('mobile/',views.mobile,name='mobile'),
    path('fullstack/',views.fullstack,name='fullstack'),
    path('machinelearning/',views.machinelearning,name='machinelearning'),
    path('backend',views.backend,name='backend'),
    
    
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('success/',views.success,name='success'),
    path('loginsuccess/',views.loginsuccess,name='loginsuccess'),
    path('users/',include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
