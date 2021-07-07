from django.shortcuts import render
from rest_framework import generics
from .models import HandbookElement, HandbookElementFilter
from .serializers import HandbookElementListSerializer, HandbookElementListSerializerValidate
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class HandbookElementListView(generics.ListAPIView):
    serializer_class = HandbookElementListSerializer
    queryset = HandbookElement.objects.all()


class HandbookElementFilterListView(generics.ListAPIView):
    serializer_class = HandbookElementListSerializer
    queryset = HandbookElement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HandbookElementFilter


class HandbookElementValidateListView(generics.ListAPIView):
    serializer_class = HandbookElementListSerializerValidate
    queryset = HandbookElement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HandbookElementFilter

