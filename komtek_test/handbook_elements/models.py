from django.db import models
from handbooks.models import Handbook
from django_filters import rest_framework as filters
# Create your models here.


class HandbookElement(models.Model):
    """
    Создаем ORM представление элементов словарей
    """
    id = models.CharField(verbose_name='id', db_index=True, primary_key=True, max_length=64, unique=True)
    fk_handbook = models.ForeignKey(Handbook, on_delete=models.CASCADE)
    code = models.CharField(max_length=15)
    value = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"

class HandbookElementFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class HandbookElementFilter(filters.FilterSet):
    """
    Формируем фильты для поиска по API
    version - версия словаря
    fk_handbook - id словаря
    """
    version = HandbookElementFilterInFilter(field_name='fk_handbook__version', lookup_expr='in') #lookup_expr='gte' - условие больше или равно..
    fk_handbook = HandbookElementFilterInFilter(field_name='fk_handbook', lookup_expr='in')
    class Meta:
        model = HandbookElement
        fields = ['version', 'fk_handbook']