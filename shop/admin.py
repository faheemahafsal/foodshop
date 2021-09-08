from django.contrib import admin
from .models import *

# Register your models here.
class catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name' ,)}
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availability','category']
    list_editable = ['price','stock','availability','category']
    prepopulated_fields = {'slug':('name' ,)}
admin.site.register(products,prodadmin)
