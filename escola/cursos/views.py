from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
"""
    API V1
"""
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

"""
    API V2
"""
class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self,request,pk=None):
        self.pagination_class.page_size=1
        avaliacoes=Avaliacao.objects.filter(curso_id=pk)
        page=self.paginate_queryset(avaliacoes)
        if page:
            serializer=AvaliacaoSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)
        #curso=self.get_object()
        serializer=AvaliacaoSerializer(avaliacoes,many=True)
        return Response(serializer.data)

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset=Avaliacao.objects.all()
    serializer_class=AvaliacaoSerializer
"""

class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
    ):
    queryset=Avaliacao.objects.all()
    serializer_class=AvaliacaoSerializer