from django.urls import path
from . import views
from .views import update_profile
from django.conf.urls.static import static
from django.conf import settings
from .views import view_u_technician_profile
from .views import view_technician_profile

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('technician/', views.technician, name='technician'),
    path('technician_list/', views.technician_list, name='technician_list'),
    path('view_u_technician_profile/', view_u_technician_profile, name='technician_profile'),
     path('view_technician_profile/', view_technician_profile, name='technician_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('logout/', views.logout_view, name='logout_view'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
