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
]
