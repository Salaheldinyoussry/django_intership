from django.db import models

# Create your models here.


class company(models.Model):
   # country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=590, null=True)
    cm1 = models.CharField(max_length=2, null=True)
    cm2 = models.CharField(max_length=2, null=True)
    cm3 = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.name