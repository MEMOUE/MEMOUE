from django.urls import path

from resto.views import CreateMenu, ListMenu, UpdateMenu, DeleteMenu

urlpatterns = [
    path("", ListMenu.as_view(), name="home-resto"),
    path("add-menu/", CreateMenu.as_view(), name="add-menu"),
    path("update-menu/<int:id>", UpdateMenu.as_view(), name="update-menu"),
    path("delete-menu/<int:id>", DeleteMenu.as_view(), name="delete-menu"),
]