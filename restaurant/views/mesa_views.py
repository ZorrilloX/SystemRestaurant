from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from restaurant.models import Mesa

class MesaListView(ListView):
    model = Mesa
    template_name = "restaurant/mesa/list.html"

class MesaCreateView(CreateView):
    model = Mesa
    template_name = "restaurant/mesa/form.html"
    fields = "__all__"
    success_url = "/restaurant/mesas/"

class MesaUpdateView(UpdateView):
    model = Mesa
    template_name = "restaurant/mesa/form.html"
    fields = "__all__"
    success_url = "/restaurant/mesas"

class MesaDeleteView(DeleteView):
    model = Mesa
    success_url = reverse_lazy("mesas")
