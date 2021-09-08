from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):

    def __str__(self):
        return self.name
    name=models.CharField(max_length = 250,unique = True)
    slug=models.SlugField(max_length = 250,unique = True)

    class Meta :
        ordering=('name',)
        verbose_name='categories'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class products(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length = 250,unique = True)
    slug=models.CharField(max_length = 250,unique = True)
    img=models.ImageField(upload_to = 'product')
    desc=models.TextField()
    stock=models.IntegerField()
    availability=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete = models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])