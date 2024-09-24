from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('product/', views.product_list, name='products'),
    path('product/product-detail/<str:id>/',views.ProductDetail,name='productdetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)