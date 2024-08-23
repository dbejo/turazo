from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=False)
        return super().save(*args, **kwargs)
    
class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=False)
        return super().save(*args, **kwargs)
    
class Photo(models.Model):
    description = models.CharField(max_length=120, null=True, blank=True)
    photographer = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.image.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null = False, unique=True)
    banner = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=False)
        return super().save(*args, **kwargs)
    
