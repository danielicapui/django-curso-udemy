from django.urls import path
from .views import CursoAPIView,AvaliacaoAPIView,CursosAPIView,AvaliacoesAPIView
#app_name ='cursos'
urlpatterns = [
    #path('<int:question_id>/vote/',views.cadastro,name='cadastro'),
    #path('cadastro/',cadastro,name='cadastro'),
    path('cursos/',CursosAPIView.as_view(),name='cursos'),
    path('avaliacoes/',AvaliacoesAPIView.as_view(),name='avaliacoes'),
     path('cursos/<int:pk>',CursoAPIView.as_view(),name='curso'),
    path('avaliacoes/<int:pk>',AvaliacaoAPIView.as_view(),name='avaliacao'),
]