from django.urls import path

from .views import list_receitas, detalhes_receita

app_name = "receitas"

urlpatterns = [
    path('', list_receitas, name="list"),
    path('<int:receita_id>/detalhes/', detalhes_receita, name="detalhes")
]
