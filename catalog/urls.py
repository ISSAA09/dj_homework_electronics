from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, CategoryListView, ProductListView, BlogListView,BlogCreateView,BlogUpdateView,BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='electronic_category'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
]
