
from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length = 30, verbose_name = "Title")

    def __str__(self):
        return self.title

class SneakerCard(models.Model):
    title = models.CharField(max_length = 30, verbose_name = "Title")
    description = models.TextField(verbose_name = "Description")
    image = models.ImageField(upload_to='main', verbose_name = 'Image')
    price = models.IntegerField(verbose_name = "Price")
    category = models.ForeignKey(Brand, verbose_name = "Brand", on_delete = models.CASCADE)