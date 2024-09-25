from django.urls import path
from.import views
urlpatterns = [
    path('contact/',views.contact,name="contacts"),
    path('contact-store/',views.store_contact,name="contact-store"),
]
