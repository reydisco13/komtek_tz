from django.shortcuts import render
from rest_framework import generics
from .models import Handbook, HandbookFilter
from .serializers import HandbookListSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class HandbookListView(generics.ListAPIView):
    serializer_class = HandbookListSerializer
    queryset = Handbook.objects.all()


class HandbookFilterListView(generics.ListAPIView):
    serializer_class = HandbookListSerializer
    queryset = Handbook.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HandbookFilter