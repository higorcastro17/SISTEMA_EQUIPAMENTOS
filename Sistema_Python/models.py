from django.db import models

class Equipamento(models.Model):
 MAC = models.CharField(
 primary_key=True, 
 max_length=20,
 null=False,
 blank=False
)

 Numero_Patrimonio = models.CharField(
 max_length=50,
 null=False,
 blank=False
 )

 Processador = models.CharField(
 max_length=50,
 null=False,
 blank=False
 )


 

class Cliente(models.Model):
 Nome = models.CharField(
 max_length=15,
 null=False,

 )
 
 

 
objects = models.Manager()
