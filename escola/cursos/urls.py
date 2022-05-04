from django.urls import path
from .views import cadastro,CursoAPIView,AvaliacaoAPIView
#app_name ='cursos'
urlpatterns = [
    #path('<int:question_id>/vote/',views.cadastro,name='cadastro'),
    path('cadastro/',cadastro,name='cadastro'),
    path('cursos/',CursoAPIView.as_view(),name='cursos'),
    path('avaliacoes/',AvaliacaoAPIView.as_view(),name='avaliacoes'),
]