from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index,categories,electronic_category

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/electronics/', electronic_category, name='electronic_category'),
]
