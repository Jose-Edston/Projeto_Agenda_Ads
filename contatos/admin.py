from django.contrib import admin
from .models import Contatos

# Essa classe serve para customizar a página de Admin
class AdminContatos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf', 'ativo']
    # para criar um campo de busca e as possibilidades de busca
    search_fields = ['nome']
    # para criar um filtro vendo só os ativos (poderia ser por categoria, classe, etc...)
    list_filter = ['ativo']
    # para criar um link, onde ao clicar, ele leva para a configuração do item
    list_display_links =['nome']


admin.site.register(Contatos, AdminContatos)


