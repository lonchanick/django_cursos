from django.contrib import admin
from rango.models import Page, Category
# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url','views')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}
	exclude=['views','likes']
	#readonly_fields=['slug'] #no esposible hace readonly un campo que se autorellena
		

admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)



