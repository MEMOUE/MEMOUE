from django.urls import path

from configuration.views import home_config, CreateConfig, DetailConfig, ListConfig, regle_prix, ListRegle, update_config, \
    UpdateConfig, update_rule, delete_rule

app_name = "confighotel"
urlpatterns = [
    path("", home_config, name="home-config"),
    path("create-rule/", regle_prix, name="create-rule"),
    path("list-rule/", ListRegle.as_view(), name="list-rule"),
    path("update-rule/<int:id>", update_rule, name="update-rule"),
    path("delete-rule/<int:id>", delete_rule, name="delete-rule"),
    path("create/", CreateConfig.as_view(), name="create-config"),
    path("list/", ListConfig.as_view(), name="list-config"),
    path("detail/<int:pk>", DetailConfig.as_view(), name="detail-config"),
    path("update-config/<int:pk>", UpdateConfig.as_view(), name="update-config"),
    path("update-config/", update_config, name="update-config"),
]