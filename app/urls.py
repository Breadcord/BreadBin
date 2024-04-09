from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.simple_index, name='simple_index'),
    path('simple/<module_id>/', views.simple_module, name='simple_module'),
    path('package/<module_id>/<file_name>', views.download_package, name='download_package'),
]
