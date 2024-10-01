from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.admin_home,name="admin_home"),
    path('admin_product/', views.admin_product, name="admin_product"),
    path('admin_add_category/', views.admin_add_category, name='admin_add_category'),
    path("admin_add_category_validation/", views.admin_add_category_validation, name = "admin_add_category_validation"),
    path("add_product/", views.add_product, name = "add_product"),
    path("admin_add_product_validation/", views.admin_add_product_validation, name = "admin_add_product_validation"),
    path('admin_account/',views.admin_account,name="admin_account"),
    path('admin_login/',views.admin_login,name="admin_login"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

