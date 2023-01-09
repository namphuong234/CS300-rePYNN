from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # additional
    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='dishes/%Y/%m/%d', blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish', args=[str(self.id)])
