from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_test import views

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('buy/<int:pk>/', views.buy_product),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
