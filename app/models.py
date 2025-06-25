from django.db import models

class Card(models.Model):
    url = models.ImageField(upload_to="cards/", null=True, blank=True, verbose_name="Изображение")
    title = models.CharField(max_length=256, verbose_name="Модель Машины")
    description = models.CharField(max_length=3000, verbose_name="Краткое Описание")
    parameters = models.CharField(max_length=3000, verbose_name="Параметры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Посты"