from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from restaurant.models import Mesero

class MeseroListView(ListView):
    model = Mesero
    template_name = "restaurant/mesero/list.html"


class MeseroCreateView(CreateView):
    model = Mesero
    template_name = "restaurant/mesero/form.html"
    fields = "__all__"
    success_url = "/restaurant/meseros"


class MeseroUpdateView(UpdateView):
    model = Mesero
    template_name = "restaurant/mesero/form.html"
    fields = "__all__"
    success_url = "/restaurant/meseros"


class MeseroDeleteView(DeleteView):
    model = Mesero
    success_url = reverse_lazy("meseros")
