from django.db import models
from django.db.models import Avg

from datetime import timedelta

class Coin(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    description = models.TextField()
    image = models.ImageField(upload_to='coins')

    def __str__(self):
        return self.name
    
    def get_last_day(self):
        return self.transaction.all().order_by('-date').first().date.date()
    
    def get_average_transactions_by_date(self, date):
        return self.transaction.filter(date = date).aggregate(average = Avg('price'))
    
    def get_last_five_days_data(self):
        data = []
        last_day = self.get_last_day()
        for i in range(1, 6):
            data.append(self.get_average_transactions_by_date(last_day)['average'])
            last_day -= timedelta(days = 1)
        return data

class Transaction(models.Model):

    CHOICE = (
        ('buy', 'buy'),
        ('sell', 'sell'),
    )

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name = 'transactions')
    price = models.FloatField()
    amount = models.FloatField()
    date = models.DateField()
    transaction_type = models.CharField(max_length=4, choices=CHOICE)

    def __str__(self):
        return self.coin.name + ' ' + self.transaction_type
    
    @classmethod
    def get_last_day(cls):
        return cls.objects.all().order_by('-date').first().date.date()
