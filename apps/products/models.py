from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]
