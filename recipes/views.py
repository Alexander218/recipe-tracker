from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

# Displays an individual recipe by its id
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)

# Lists all currently stored recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list":recipes,
    }
    return render(request,"recipes/list.html",context)

# Creates a new recipe using form
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }
    return render(request, "recipes/create.html", context)

# Modify/edit a recipe
def edit_recipe(request, id):
    post = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=post.id)
    else:
        form = RecipeForm(instance=post)

    context = {
        "post_recipe": post,
        "form": form,
    }
    return render(request, "recipes/edit.html", context)
