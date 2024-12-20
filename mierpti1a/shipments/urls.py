# shipments/urls.py
from django.urls import path
from .views import order_list, order_create, order_detail, route_detail, order_edit, order_delete, listar_sucursales, agregar_sucursal, eliminar_sucursal


app_name = 'shipments'

urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('orders/create/', order_create, name='order_create'),
    path('orders/<int:id>/', order_detail, name='order_detail'),
    path('orders/<int:pk>/route/', route_detail, name='route_detail'),  # Confirmar que esta ruta esté definida
    path('orders/edit/<int:pk>/', order_edit, name='order_edit'),
    path('orders/delete/<int:id>/', order_delete, name='order_delete'),
    path('sucursales/', listar_sucursales, name='listar_sucursales'),
    path('sucursales/agregar/', agregar_sucursal, name='agregar_sucursal'),
    path('sucursales/eliminar/<int:pk>/', eliminar_sucursal, name='eliminar_sucursal')

]

urlpatterns = [
]