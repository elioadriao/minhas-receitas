from django.shortcuts import render

from .models import Receita


def list_receitas(request):
    receitas = Receita.objects.all()
    return render(request, "receita/list.html", {'receitas': receitas})


def detalhes_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    return render(request, "receita/detalhes.html", {"receita": receita})
