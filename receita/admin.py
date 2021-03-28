from django.contrib import admin

from .models import Receita, Ingrediente


class IngredienteAdmin(admin.TabularInline):
    model = Ingrediente
    extra = 0


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_refeicao", "nivel_dificuldade", )
    list_display_links = list_display
    inlines = [IngredienteAdmin]
