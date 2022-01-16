from django.db import models


class Region(models.Model):
    class Meta:
        db_table = 'Region'
        ordering = ['name']

    class RegionsChoices(models.TextChoices):
        NORTE = 'Norte'
        NORDESTE = 'Nordeste'
        CENTRO_OESTE = 'Centro-Oeste'
        SUDESTE = 'Sudeste'
        SUL = 'Sul'

    name = models.CharField(
        max_length=12,
        choices=RegionsChoices.choices,
        unique=True,
    )


class Fruit(models.Model):
    class Meta:
        db_table = 'Fruit'
        ordering = ['name']

    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(
        to=Region, on_delete=models.SET_NULL, null=True)
