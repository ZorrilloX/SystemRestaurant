from django.contrib import admin
from django.urls import path
from . import views
from .views.panel_views import InicioView

urlpatterns = [
       path("admin/", admin.site.urls),
       path('panel', InicioView.as_view(), name='index'),

       path("clientes/", views.ClienteListView.as_view(),name="clientes"),
       path("clientes/create/", views.ClienteCreateView.as_view(), name="clientes_create"),
       path("clientes/<int:pk>/", views.ClienteUpdateView.as_view(), name="clientes_update"),
       path("clientes/<int:pk>/delete/", views.ClienteDeleteView.as_view(), name="clientes_delete"),

       path("meseros/", views.MeseroListView.as_view(), name="meseros"),
       path("meseros/create/", views.MeseroCreateView.as_view(), name="meseros_create"),
       path("meseros/<int:pk>/", views.MeseroUpdateView.as_view(), name="meseros_update"),
       path("meseros/<int:pk>/delete/", views.MeseroDeleteView.as_view(), name="meseros_delete"),

       path("mesas/", views.MesaListView.as_view(), name ="mesas"),
       path("mesas/create/", views.MesaCreateView.as_view(), name="mesas_create"),
       path("mesas/<int:pk>/", views.MesaUpdateView.as_view(), name="mesas_update"),
       path("mesas/<int:pk>/delete/", views.MesaDeleteView.as_view(), name="mesas_delete"),

       path("platos/", views.PlatoListView.as_view(), name ="platos"),
       path("platos/create/", views.PlatoCreateView.as_view(), name="platos_create"),
       path("platos/<int:pk>/", views.PlatoUpdateView.as_view(), name="platos_update"),
       path("platos/<int:pk>/delete/", views.PlatoDeleteView.as_view(), name="platos_delete"),



       path("ordenes/", views.OrdenListView.as_view(), name="ordenes"),
       path("ordenes/create/", views.OrdenCreateView.as_view(), name="ordenes_create"),
       path("ordenes/<int:pk>/update/", views.OrdenUpdateView.as_view(), name="ordenes_update"),
       path("ordenes/<int:pk>/delete/", views.OrdenDeleteView.as_view(), name="ordenes_delete"),
       # ruta para el pago: se actualizan los datos del cliente y se cierra la orden
       path("ordenes/<int:pk>/pagar/", views.OrdenPagarUpdateView.as_view(), name="ordenes_pagar"),
]
