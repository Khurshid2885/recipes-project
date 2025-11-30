from django.db import models

from apps.accounts.models import User
from apps.core.models import BaseModel


class RecipeCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Recipe Category"
        verbose_name_plural = "Recipe Categories"
        ordering = ["name"]
        db_table = "recipe_category"

    def __str__(self):
        return self.name


class Recipe(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)


class Ingredient(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)


class Step(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField()
