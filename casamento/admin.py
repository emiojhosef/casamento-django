from django.contrib import admin
from casamento.models import ListaPresente, Convidado, MembroDaFamilia

class ListandoPresentes(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(ListaPresente, ListandoPresentes)

class ListandoConvidado(admin.ModelAdmin):
    list_display = ("id", "nome", "telefone", "senha", "confirmado", "confirmado_2")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 10

admin.site.register(Convidado, ListandoConvidado)

class ListandoMembro(admin.ModelAdmin):
    list_display = ("id", "nome", "convidado", "confirmado")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 10

admin.site.register(MembroDaFamilia, ListandoMembro)
