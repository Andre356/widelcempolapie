from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=128)
    portions = models.IntegerField(default=2, null=True, blank=True)
    ingredients = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    added = models.DateField(null=True, blank=True)                       # blank działa na rekordy w db
    photo0 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.IntegerField(default=0)
    thermomix = models.BooleanField(default=False, blank=True)

    def dateformat(self):
        return self.added.strftime('%e.%m.%Y')

    def __str__(self):
        return self.name
