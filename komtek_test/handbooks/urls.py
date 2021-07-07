from django.urls import path
from .views import HandbookListView, HandbookFilterListView

urlpatterns = [
    path('all/', HandbookListView.as_view()),
    path('transaction/all/', HandbookFilterListView.as_view()),
]