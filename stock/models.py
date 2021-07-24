from django.db import models

class Stock(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Information(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.CharField(max_length=7)
    sales = models.IntegerField()
    profit = models.IntegerField()

    def __str__(self):
        return self.stock.name + ' (' + self.date + ')'

