from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='cat_pics/', null=True, blank=True)
    active = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('detail_product', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.category + str(self.pk)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(max_length=1024, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='product_pics/', help_text='Primary', null=True, blank=True)
    image_2 = models.ImageField(upload_to='product_pics/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='product_pics/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='product_pics/', null=True, blank=True)
    image_5 = models.ImageField(upload_to='product_pics/', null=True, blank=True)
    image_6 = models.ImageField(upload_to='product_pics/', null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('detail_product', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name + str(self.pk)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
