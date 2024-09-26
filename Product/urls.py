from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/', views.product_list, name='products'),
    path('add_product/', views.add_product, name='add_products'),
    path('product/product-detail/<str:id>/',views.ProductDetail,name='productdetail'),
    path('store_product/', views.store_product, name='store_products'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)