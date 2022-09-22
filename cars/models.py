from django.db import models

# # Representations of the table and the database
# Create your models here.
            # models.Model (prepackaged Django function)
class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)