from django.db import models

# Create your models here.
class Category(models.Model):
    nom=models.CharField(max_length=250)
    date_ajout=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_ajout']

    def __str__(self):
        return self.nom

class Product(models.Model):
    nom=models.CharField(max_length=250)
    prix=models.FloatField()
    description=models.TextField()
    categorie=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    date_ajout=models.DateTimeField(auto_now_add=True)
    quantite_en_stock = models.PositiveIntegerField(default=0) 
    class Meta:
        ordering=['-date_ajout']

   
    def quantite_disponible(self):
        if self.quantite_en_stock > 5:
            return 'green'
        elif 0 < self.quantite_en_stock <= 5:
            return 'orange'
        else:
            return 'red'
    

    def __str__(self):
        return self.nom