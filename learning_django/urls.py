from django.contrib import admin
from django.urls import path
from api_test import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('admin/', admin.site.urls),
]
