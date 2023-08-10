from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True ,null = True ,blank=True)
    category_image = models.ImageField(upload_to='categories')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name
    
class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color_name

class SizeVariant(BaseModel):
    price = models.IntegerField(default=0)
    size_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        
        return self.size_name
    
class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant)
    size_Variant = models.ManyToManyField(SizeVariant)
    
class ProductImages(BaseModel):
    products = models.ForeignKey(Products,on_delete=models.CASCADE , related_name="product_Images")
    image =  models.ImageField(upload_to="product",null=True, blank = True)
