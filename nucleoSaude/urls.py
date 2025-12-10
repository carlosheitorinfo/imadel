from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('contato/', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
    path('login/', views.login_view, name='login'),
    path('perfil/',views.perfil ,name='perfil'),
    path('medicos/',views.medicos ,name='medicos'),
    path('pacientes/',views.pacientes ,name='pacientes'),
    path('agendamento/',views.agendamento ,name='agendamento'),
    path('registrar/',views.registrar_view ,name='registrar'),
    
]