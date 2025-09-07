from django.db import models

# Create your models here.

class Product(models.Model):

    # category choices
    category_choices = [
        ('outdoor', 'Outdoor Items'),
        ('indoor', 'Indoor Items')
    ]

    # required columns
    name = models.CharField(max_length=255) 
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField() # sebagai tempat menyimpan link gambar dari produk
    category = models.CharField(max_length=50, choices=category_choices) 
    is_featured = models.BooleanField(default=False) # status unggulan item
    # adding more columns I insisted
    stock = models.PositiveIntegerField(default=0) # tempat menyimpan banyaknya stock dari produk
    created_at = models.DateTimeField(auto_now_add=True) # tempat menyimpan tanggal dibuatnya sebuah produk
    updated_at = models.DateTimeField(auto_now=True) # tempat menyimpan tanggal setiap produk mengalami perubahan

    # sebagai representasi string dari setiap object Product
    def __str__(self):
        return self.name