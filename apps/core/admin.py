from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.accounts.models import User
from apps.recipes.models import RecipeCategory, Recipe, Ingredient, Step


# Register your models here.
@admin.register(User)
class UserModelAdmin(ModelAdmin):
    pass


@admin.register(RecipeCategory)
class RecipeCategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeModelAdmin(ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientModelAdmin(ModelAdmin):
    pass


@admin.register(Step)
class StepModelAdmin(ModelAdmin):
    pass
