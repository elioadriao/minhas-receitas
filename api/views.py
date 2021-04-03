from rest_framework import viewsets
from receita.models import Receita, Ingrediente
from .serializers import ReceitaSerializer, IngredienteSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

