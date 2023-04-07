from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Марка")
    gos_num = models.CharField(max_length=10, verbose_name="Гос номер")
    model = models.CharField(max_length=100, verbose_name="Модель")
    color = models.CharField(max_length=100, verbose_name="Цвет")

    def __str__(self):
        return self.gos_num
    
    class Meta:
       verbose_name = "Машина"
       verbose_name_plural = "Машины" 

