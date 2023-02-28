"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from resources.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('api_schema/', get_schema_view(
        title='DJANGO REST API - Resources API Documentation',
        description = \
        """
        API RESTful que permite que os usuários criem, leiam, atualizem e excluam recursos. 
        A implementação foi feita utilizando django-rest-framework com autenticação e documentação personalizada.
        """
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('recursos/', RecursoListCreateView.as_view(), name='recurso-list-create'),
    path('recursos/<int:pk>/', RecursoRetrieveUpdateDestroyView.as_view(), name='recurso-retrieve-update-destroy'),
    path('user/create/', UserCreateView.as_view(), name='signup'),
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', UserLogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
