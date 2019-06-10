from .models import CPod
from .models import CDesenvolvimento
from django.contrib import admin

class MyModelAdmin(admin.ModelAdmin):
	class Media:
		js = ('js/admin/my_own_admin.js',)
		css = {
			'all':('css/admin/my_own-admin.css',)
		}
	


admin.site.register(CPod, CDesenvolvimento, ItemDesenvolvimento, Tarefas, Escopo)
