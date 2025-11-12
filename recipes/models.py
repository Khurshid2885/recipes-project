from django.db import models

from apps.core.models import BaseModel


class RecipeCategory(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
