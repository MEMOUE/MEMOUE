from django.contrib import admin

from configuration.models import Configuration, Categories

# Register your models here.


class AdminConfiguration(admin.ModelAdmin):
    list_display = ("nom", "adresse", "telephone", "date_ajout")

    class Media:
        js = ("js/admin.js", )
        css = {
            "all": ("css/admin.css", )
        }


class AdminCategorie(admin.ModelAdmin):
    list_display = ("categorie", "prix_enfant", "prix_adulte")

    class Media:
        js = ("js/admin.js", )
        css = {
            "all": ("css/admin.css", )
        }


admin.site.register(Configuration, AdminConfiguration)
admin.site.register(Categories, AdminCategorie)