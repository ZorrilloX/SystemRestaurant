from django.views.generic import TemplateView
#este apartado es el panel de control de los diferentes views
#para mostrarlos de mejor manera
class InicioView(TemplateView):
    template_name = 'restaurant/index.html'
