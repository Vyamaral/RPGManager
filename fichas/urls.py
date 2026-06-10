from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personagens, name='lista'),
    path('novo/', views.criar_personagem, name='criar'),
    path('editar/<int:id>/', views.editar_personagem, name='editar'),
    path('excluir/<int:id>/', views.excluir_personagem, name='excluir'),
    path('cadastro/', views.cadastro, name='cadastro'),
]