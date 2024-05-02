from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('products/', views.product_list, name='products'),
    path('technician/<int:product_id>/', views.choose_technician, name='choose_technician')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
