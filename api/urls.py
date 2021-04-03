from rest_framework import routers
from .views import ReceitaViewSet, IngredienteViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("receitas", ReceitaViewSet)
router.register("ingredientes", IngredienteViewSet)

app_name = "api"

urlpatterns = [
    path('', include(router.urls))
]