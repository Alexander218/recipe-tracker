from django.urls import path
from recipes.views import show_recipe, recipe_list


urlpatterns = [
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/", recipe_list, name="recipe_list"),
]
