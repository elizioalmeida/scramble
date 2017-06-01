from django.contrib import admin

from .models import CPod, Escopo, CDesenvolvimento

from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.



#class ChoiceInline(admin.StackedInline):

class ChoiceInline(admin.TabularInline):
    model = Escopo
    extra = 3

    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
    }





class ChoiceInline1(admin.TabularInline):
    model = CDesenvolvimento
    extra = 3


    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':30})},
        models.DecimalField: {'widget': TextInput(attrs={'size':10})}
    }



class CPodAdmin(admin.ModelAdmin):

    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }

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

    inlines = [ChoiceInline, ChoiceInline1]
    #inlines = [ChoiceInline1]
    list_display = ( 'nome_cp', 'cliente', 'data_ini', 'data_fim', 'data_des_ini')
    list_filter = ['nome_cp']

class CDesenvolvimentoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['cpod']}),
        (None,  {'fields': ['nome_cd']}),
        (None,  {'fields': ['desenvolvedor']}),
        (None,  {'fields': ['descricao']}),
        (None,  {'fields': ['data_des_ini']}),
        (None,  {'fields': ['data_des_fim']}),
        (None,  {'fields': ['obs']}),
        (None,  {'fields': ['participacao']}),

    ]

    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }



    list_display = ('nome_cd', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs')
    list_filter = ['nome_cd']


admin.site.register(CPod, CPodAdmin)
admin.site.register(CDesenvolvimento, CDesenvolvimentoAdmin)
