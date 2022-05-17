from rest_framework import serializers
from django.db.models import Avg
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

    def validate_avaliacao(self,valor):
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliação está fora do range de 1 a 5')

class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship abordagem que mostra os dados e relações
    #avaliacoes=AvaliacaoSerializer(many=True,read_only=True)
    
    #HyperLinked Related Field abordagem que mostra os links
    #avaliacoes=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='avaliacao-detail')
    
    #Primary Key related Field abordagem 
    avaliacoes=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    media_avaliacoes=serializers.SerializerMethodField()

    class Meta:
        model=Curso
        fields=(
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )
        
    def get_media_avaliacoes(self,obj):
        media=obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media*2)/2
