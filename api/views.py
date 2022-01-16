from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Region, Fruit
from .serializers import RegionSerializer, FruitSerializer


@extend_schema_view(
    list=extend_schema(summary='Obtém todas as regiões'),
    create=extend_schema(summary='Insere uma nova região.'),
    retrieve=extend_schema(summary='Obtém uma região.'),
    update=extend_schema(summary='Atualiza uma região.'),
    partial_update=extend_schema(summary='Atualiza parcialmente uma região.'),
    destroy=extend_schema(summary='Remove uma região.'),
)  # Documentação
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


@extend_schema_view(
    list=extend_schema(summary='Obtém todas as frutas.'),
    create=extend_schema(summary='Insere uma nova fruta.'),
    retrieve=extend_schema(summary='Obtém uma fruta.'),
    update=extend_schema(summary='Atualiza uma fruta.'),
    partial_update=extend_schema(summary='Atualiza parcialmente uma fruta.'),
    destroy=extend_schema(summary='Remove uma fruta.'),
)  # Documentação
class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
