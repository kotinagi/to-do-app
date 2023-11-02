from django.db import models

# Create your models here.
class Product(models.Model):
# each class variable represents a database i.e. table field in the model
    id = models.CharField(max_length=200,primary_key=True)
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    quantity = models.FloatField()

    def __str__(self):
        return self.id