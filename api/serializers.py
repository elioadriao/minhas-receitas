from rest_framework import serializers
from receita.models import Receita, Ingrediente


class ReceitaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=100)
    tipo_refeicao = serializers.ChoiceField(choices=Receita.MEAL_TYPE_CHOICES)
    nivel_dificuldade = serializers.ChoiceField(choices=Receita.DIFFICULTY_LEVEL_CHOICES)
    numero_pessoa = serializers.IntegerField()
    estapas_preparacao = serializers.CharField()

    def create(self, validated_data):
        return Receita.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.tipo_refeicao = validated_data.get('tipo_refeicao', instance.tipo_refeicao)
        instance.nivel_dificuldade = validated_data.get('nivel_dificuldade', instance.nivel_dificuldade)
        instance.numero_pessoa = validated_data.get('numero_pessoa', instance.numero_pessoa)
        instance.estapas_preparacao = validated_data.get('estapas_preparacao', instance.estapas_preparacao)
        instance.save()
        return instance


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__' 
