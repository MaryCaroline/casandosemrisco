from django.contrib import admin
from core.models import Servico, Fornecedor, Avaliacao, Comentario, Denuncia, Categoria, Telefone


admin.site.register(Servico)
admin.site.register(Categoria)
admin.site.register(Avaliacao)
admin.site.register(Comentario)
admin.site.register(Denuncia)

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1

class FornecedorAdmin(admin.ModelAdmin):
    inlines = (AvaliacaoInline, TelefoneInline, )

admin.site.register(Fornecedor, FornecedorAdmin)