from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        return self.name

GEAR_CHOICES = (
    (0, 'manuel'),
    (1, 'auto'),
    (2, 'semi-auto'),
)

FUEL_CHOICES = (
    (0, 'diesel'),
    (1, 'motorin'),
    (2, 'hybrid'),
    (3, 'electric'),
)

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    gear = models.IntegerField(choices=GEAR_CHOICES, null=True)
    seat = models.SmallIntegerField(null=True)
    fuel_type = models.IntegerField(choices=FUEL_CHOICES, null=True)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name