from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso,Avaliacao
from .serializers import CursoSerializer,AvaliacaoSerializer

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def cadastro(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=certidao_cadastro.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    doc="Digite aqui o texto que irá aparecer no pdf"
    #coordenadas de onde será digitado 
    x,y=[3,3]
    p.drawString(x,y,doc)
    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
    return response

class CursoAPIView(APIView):
    """
    API de Cursos do django
    """
    def get(self,request):
        cursos=Curso.objects.all()
        serializer=CursoSerializer(cursos,many=True)
        return Response(serializer.data)
    
class AvaliacaoAPIView(APIView):
    """
    API de Avaliacao do django
    """
    def get(self,request):
        avaliacoes=Avaliacao.objects.all()
        serializer=AvaliacaoSerializer(avaliacoes,many=True)
        return Response(serializer.data)