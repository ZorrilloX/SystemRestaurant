from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from restaurant.models import Plato

class PlatoListView(ListView):
    model = Plato
    template_name = "restaurant/plato/list.html"

class PlatoCreateView(CreateView):
    model = Plato
    template_name = "restaurant/plato/form.html"
    fields = "__all__"
    success_url = "/restaurant/platos/"

class PlatoUpdateView(UpdateView):
    model = Plato
    template_name = "restaurant/plato/form.html"
    fields = "__all__"
    success_url = "/restaurant/platos"

class PlatoDeleteView(DeleteView):
    model = Plato
    success_url = reverse_lazy("platos")