from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset=Avaliacao.objects.all()
    serializer_class=AvaliacaoSerializer

    def get_queryset(self):
        #kwargs pega o int:curso_pk da uri
        id=self.kwargs.get('curso_pk')
        if id:
            return self.queryset.filter(curso_id=id)
        return self.queryset.all()

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Avaliacao.objects.all()
    serializer_class=AvaliacaoSerializer
    
    def get_object(self):
        curso_pk=self.kwargs.get('curso_pk')
        avaliacao_pk=self.kwargs.get('avaliacao_pk')
        if curso_pk:
            return get_object_or_404(self.get_queryset(),curso_id=curso_pk,pk=avaliacao_pk)
        return get_object_or_404(self.get_queryset(),pk=avaliacao_pk)