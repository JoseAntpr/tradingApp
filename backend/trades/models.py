from django.db import models
from django.utils.crypto import get_random_string


class TypeMoney(models.Model):
    """ TypeMoney Model"""
    name = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.name


def create_id(self):
        """ Return a id
    
        Method for create a custom id
        """
        return "PR" + get_random_string(length=7)


class Trade(models.Model):
    """ Trade model """
    my_id = models.CharField(
        max_length=9, primary_key=True, editable=False, 
        default=create_id)
    sell_currency = models.ForeignKey(
        TypeMoney, related_name="sell_currency", on_delete=models.CASCADE)
    sell_amount = models.DecimalField(max_digits=10, decimal_places=2)
    buy_currency = models.ForeignKey(
        TypeMoney, related_name="buy_currency", on_delete=models.CASCADE)
    buy_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=5)
    date_booked = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.sell_currency) + "-->" + str(self.buy_currency)


    class Meta:
        ordering = ['-date_booked']

    
