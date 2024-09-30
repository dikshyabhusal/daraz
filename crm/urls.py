from django.urls import path
from .import views

urlpatterns = [
    path('',views.admin_home,name="admin_home"),
    path('admin_product/', views.admin_product, name="admin_product"),
    path('admin_add_category/', views.admin_add_category, name='admin_add_category'),
    path("admin_add_category_validation/", views.admin_add_category_validation, name = "admin_add_category_validation"),
    path("add_product/add", views.add_product, name = "add_product"),
    path("admin_add_product_validation/", views.admin_add_product_validation, name = "admin_add_product_validation"),
]

