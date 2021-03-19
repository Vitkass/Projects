from django.db import models
import django_filters




class Texture(models.Model):
    oder_number = models.CharField("Номер заказа", max_length = 50)
    material = models.CharField("Изделие", max_length = 50)
    size = models.CharField("Размер", max_length = 50)
    oder_date = models.DateTimeField("Дата заказа")
    delivery_date = models.DateTimeField("Дата сдачи")
    sn_number = models.CharField("SN", max_length = 50)
    status = models.CharField("Статус", max_length = 50)
    texture1 = models.CharField("Текстура1", max_length = 50)
    decorator1 = models.CharField("Декоратор1", max_length = 50)
    status1 = models.CharField("Статус1", max_length = 50)
    date1 = models.DateTimeField("Дата1")
    comment1 = models.CharField("Комментарий1", max_length = 200)
    texture2 = models.CharField("Текстура2", max_length = 50)
    decorator2 = models.CharField("Декоратор2", max_length = 50)
    status2 = models.CharField("Статус2", max_length = 50)
    date2 = models.DateTimeField("Дата2")
    comment2 = models.CharField("Комментарий2", max_length = 200)
    
    
    def __str__(self):
        return self.oder_number


