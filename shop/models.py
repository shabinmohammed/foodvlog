
from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Categ(models.Model):
    name=models.CharField( max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='media/product',default=True)
    dsc=models.TextField(default="")
    stock=models.IntegerField(null=True)
    available=models.BooleanField(null=True)
    price=models.IntegerField(null=True)
    category=models.ForeignKey(Categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)



