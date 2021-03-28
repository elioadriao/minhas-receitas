from django.db import models


class Receita(models.Model):

    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    SUPPER = "supper"
    SNACK = "snack"

    MEAL_TYPE_CHOICES = (
        (BREAKFAST, "Café da manhã"),
        (LUNCH, "Almoço"),
        (SUPPER, "Jantar"),
        (SNACK, "Lanche"),
    )

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

    DIFFICULTY_LEVEL_CHOICES = (
        (BEGINNER, "Iniciante"),
        (INTERMEDIATE, "Intermediário"),
        (ADVANCED, "Avançado"),
    )

    titulo = models.CharField("Titulo", max_length=100)
    tipo_refeicao = models.CharField("Tipo de Refeição", max_length=15, choices=MEAL_TYPE_CHOICES)
    nivel_dificuldade = models.CharField("Nível de dificuldade", max_length=15, choices=DIFFICULTY_LEVEL_CHOICES)
    numero_pessoa = models.IntegerField("Numero de pessoas que serve")
    estapas_preparacao = models.TextField("Etapas de preparo")


class Ingrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    nome = models.CharField("Nome do ingradiente", max_length=100)
    medida = models.CharField("Medida do ingrediente", max_length=50)

