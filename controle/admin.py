from django.contrib import admin

from .models import CPod, Escopo, CDesenvolvimento, ItemDesenvolvimento

from django.forms import TextInput, Textarea, ModelForm
from django.db import models
# Register your models here.



#class ChoiceInline(admin.StackedInline):

class ChoiceInline(admin.TabularInline):
    model = Escopo
    extra = 1

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }


class ChoiceInline1(admin.TabularInline):
    model = CDesenvolvimento
    extra = 1

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':30})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
        models.DecimalField: {'widget': TextInput(attrs={'size':4})}
    }

class ChoiceInline2(admin.TabularInline):
    model = ItemDesenvolvimento
    extra = 1

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':20})},
        models.DecimalField: {'widget': TextInput(attrs={'size':4})}
    }


class CPodAdmin(admin.ModelAdmin):

    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':60})},
    }

    fieldsets = [
            (None,  {'fields':['nome_cp']}),
            (None,  {'fields':['cliente']}),
            (None,  {'fields':['data_ini']}),
            (None,  {'fields':['data_fim']}),
            (None,  {'fields':['data_des_ini']}),
            (None,  {'fields':['data_des_fim']}),
            (None,  {'fields':['obs']}),
	    (None,  {'fields':['status']}),	
            # 'classes':['collapse']}),
    ]

    inlines = [ChoiceInline, ChoiceInline1]
    #inlines = [ChoiceInline1]
    list_display = ( 'nome_cp', 'cliente', 'data_ini', 'data_fim', 'data_des_ini', 'status', )
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

    inlines = [ChoiceInline2]

    list_display = ('nome_cd', 'cpod', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs', 'participacao', )
    list_filter = ['desenvolvedor', 'cpod', 'nome_cd', ]


class ItemDesenvolvimentoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['cdes']}),
        (None,  {'fields': ['nome_item']}),
        (None,  {'fields': ['descricao']}),
        (None,  {'fields': ['data_ini']}),
        (None,  {'fields': ['data_fim']}),
        (None,  {'fields': ['obs']}),
        (None,  {'fields': ['participacao']}),
        (None,  {'fields': ['concluido']}),

    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }

    list_display = ('nome_item', 'cdes', 'descricao', 'data_ini', 'data_fim', 'obs', 'participacao', 'concluido')
    list_filter = [ 'cdes', 'concluido', 'nome_item',]


admin.site.register(CPod, CPodAdmin)
admin.site.register(CDesenvolvimento, CDesenvolvimentoAdmin)
admin.site.register(ItemDesenvolvimento, ItemDesenvolvimentoAdmin)
