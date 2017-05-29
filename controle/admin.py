from django.contrib import admin

from .models import CPod, Escopo, CDesenvolvimento

# Register your models here.



#class ChoiceInline(admin.StackedInline):

class ChoiceInline(admin.TabularInline):
    model = Escopo
    extra = 3


class CPodAdmin(admin.ModelAdmin):

    fieldsets = [
            (None,  {'fields':['nome_cp']}),
            (None,  {'fields':['cliente']}),
            (None,  {'fields':['data_ini']}),
            (None,  {'fields':['data_fim']}),
            (None,  {'fields':['data_des_ini']}),
            (None,  {'fields':['data_des_fim']}),
            (None,  {'fields':['obs']}),

            # 'classes':['collapse']}),
    ]

    inlines = [ChoiceInline]
    list_display = ( 'nome_cp', 'cliente', 'data_ini', 'data_fim', 'data_des_ini')
    list_filter = ['nome_cp']

class CDesenvolvimentoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['nome_cd']}),
        (None,  {'fields': ['desenvolvedor']}),
        (None,  {'fields': ['descricao']}),
        (None,  {'fields': ['data_des_ini']}),
        (None,  {'fields': ['data_des_fim']}),
        (None,  {'fields': ['obs']}),

    ]

    list_display = ('nome_cd', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs')
    list_filter = ['nome_cd']


admin.site.register(CPod, CPodAdmin)
admin.site.register(CDesenvolvimento, CDesenvolvimentoAdmin)
