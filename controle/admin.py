from django.contrib import admin

from .models import CPod, Escopo

# Register your models here.



#class ChoiceInline(admin.StackedInline):

class ChoiceInline(admin.TabularInline):
    model = Escopo
    extra = 3


class CPodAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields':['nome_cp']}),
            ('Cliente', {'fields':['cliente'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ( 'nome_cp', 'cliente', 'data_ini', 'data_fim')
    list_filter = ['nome_cp']

admin.site.register(CPod, CPodAdmin)


