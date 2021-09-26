from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null= True)
    def __str__(self):
        return self.name

class Year(models.Model):
    date = models.IntegerField()
    def __str__(self):
        return str(self.date)

class Country(models.Model):
    cname = models.CharField(max_length=200)
    def __str__(self):
        return self.cname

class Sales(models.Model):
    sales = models.IntegerField(default=0, null= True)
    typess = models.ForeignKey(Product,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    countries = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sales)

