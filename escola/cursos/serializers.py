from rest_framework import serializers
from  .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs={
            'email':{'write_only':True}
        }
        model=Avaliacao
        #campos que irão mostrar de avaliação
        fields=(
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship abordagem que mostra os dados e relações
    #avaliacoes=AvaliacaoSerializer(many=True,read_only=True)
    
    #HyperLinked Related Field abordagem que mostra os links
    #avaliacoes=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='avaliacao-detail')
    
    #Primary Key related Field abordagem 
    avaliacoes=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Curso
        fields=(
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )