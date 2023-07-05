from django.contrib import admin

from resto.models import Restaurant

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("nom_menu", "type", "quantite", "prix", "date")
    search_fields = ["nom_menu", "type", "prix"]


    class Media:
        js = ("js/admin.js", )
        css = {
            "all": ("css/admin.css", )
        }


#admin.site.register(Restaurant)