"""
URL configuration for sistema_vacinacao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/vacinas/', include('vacinas.urls')),
    path('api/medicos/', include('medicos.urls')),
    path('api/unidades-saude/', include('unidades_saude.urls')),
    path('api/estoques-vacina/', include('estoques_vacina.urls')),
    path('api/campanhas-vacinais/', include('campanhas_vacinais.urls')),
    path('api/campanha-vacinal-vacina/', include('campanha_vacinal_vacina.urls')),
    path('api/aplicacoes-vacinais/', include('aplicacoes_vacinais.urls')),
    path('api/agendamentos/', include('agendamentos.urls')),
]
