from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from restaurant.models import Orden


class OrdenListView(ListView):
    model = Orden
    template_name = "restaurant/orden/list.html"


class OrdenCreateView(CreateView):
    model = Orden
    template_name = "restaurant/orden/form.html"
    fields = ["meseros", "platos", "mesa"]
    success_url = "/restaurant/ordenes/"


class OrdenUpdateView(UpdateView):
    model = Orden
    template_name = "restaurant/orden/form.html"
    fields = ['meseros', 'platos', 'mesa']
    success_url = "/restaurant/ordenes/"


# Eliminar una orden
class OrdenDeleteView(DeleteView):
    model = Orden
    success_url = reverse_lazy("ordenes")


# asigna datos del cliente y cierra la orden
class OrdenPagarUpdateView(UpdateView):
    model = Orden
    template_name = "restaurant/orden/pago_form.html"
    fields = ['cliente_nombre', 'cliente_nit'] # solo se muestran campos para el pago
    success_url = reverse_lazy("ordenes")

    def form_valid(self, form):
        # Verifica que los campos de cliente tengan contenido
        cliente_nombre = form.cleaned_data.get("cliente_nombre")
        cliente_nit = form.cleaned_data.get("cliente_nit")
        if not cliente_nombre or not cliente_nit:
            form.add_error(None, "Debe ingresar el nombre y el NIT del cliente.")
            return self.form_invalid(form)
        form.instance.estado = 'cerrada'
        return super().form_valid(form)



