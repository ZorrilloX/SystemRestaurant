from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from restaurant.models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = "restaurant/cliente/list.html"


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "restaurant/cliente/form.html"
    fields = "__all__"
    success_url = "/restaurant/clientes"


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "restaurant/cliente/form.html"
    fields = "__all__"
    success_url = "/restaurant/clientes"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")
