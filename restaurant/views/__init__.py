from .cliente_views import (ClienteListView, ClienteCreateView,
                            ClienteDeleteView, ClienteUpdateView)

from .mesero_views import (MeseroListView, MeseroCreateView,
                           MeseroDeleteView, MeseroUpdateView)

from .mesa_views import (MesaListView, MesaCreateView,
                         MesaDeleteView, MesaUpdateView)

from .plato_views import (PlatoListView, PlatoCreateView,
                          PlatoDeleteView, PlatoUpdateView)

from .orden_views import (OrdenListView, OrdenCreateView, OrdenUpdateView,
                          OrdenDeleteView, OrdenPagarUpdateView)