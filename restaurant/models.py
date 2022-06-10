from django.db import models

class Plat(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.nom + ' : ' + self.ingredients
