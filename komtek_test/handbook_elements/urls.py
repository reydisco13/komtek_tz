from django.urls import path
from .views import HandbookElementListView,HandbookElementFilterListView, HandbookElementValidateListView

urlpatterns = [
    path('all/', HandbookElementListView.as_view()),
    path('filter/all/', HandbookElementFilterListView.as_view()),
    path('validate/all/', HandbookElementValidateListView.as_view()),
]