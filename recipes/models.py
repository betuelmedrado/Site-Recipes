from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipes(models.Model):

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()    
    preparation_time = models.IntegerField(default=0)
    preparation_time_unit = models.CharField(max_length=65)
    serving = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)    
    create_at = models.DateTimeField(auto_now_add=True)  # Enter the times here when recipes are created
    update_at = models.DateTimeField(auto_now=True) # insert the time when editing the recitation
    is_plubeshed = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='%Y/%m/%d/', blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.title