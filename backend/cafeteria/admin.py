from django.contrib import admin
from .models import (CafeInsumo, ReceitaDiretaAoCliente, ReceitaItem  )

admin.site.register(CafeInsumo)
admin.site.register(ReceitaDiretaAoCliente)
admin.site.register(ReceitaItem)
