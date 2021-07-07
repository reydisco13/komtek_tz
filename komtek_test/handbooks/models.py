from django.db import models
from django_filters import rest_framework as filters
# Create your models here.


class Handbook(models.Model):
    """
    Создаем ROM словарей
    """
    id = models.CharField(verbose_name='id', db_index=True, primary_key=True, max_length=64, unique=True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=350, blank=True)
    version = models.CharField(max_length=15, unique=True)
    date = models.DateField()

    class Meta:
        verbose_name = "Словарь"
        verbose_name_plural = "Список словарей"


class HandbookFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class HandbookFilter(filters.FilterSet):
    """
    Фильтр по дате
    """
    date = HandbookFilterInFilter(field_name='date', lookup_expr='in') #lookup_expr='gte'

    class Meta:
        model = Handbook
        fields = ['date']
