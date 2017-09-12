import json
from django.test import TestCase, Client
from rest_framework.response import Response
from rest_framework import status
from .models import Trade, TypeMoney
from .serializers import TradeSerializer,TypeMoneySerializer

# Initialize the APIClient app
client = Client()


class GetAllTypeMoneyTest(TestCase):
    """ Test module for GET all TypeMoney API"""

    def setUp(self):
        TypeMoney.objects.create(name="USD")
        TypeMoney.objects.create(name="EUR")
    
    def test_get_all_typeMoney(self):
        # get API response
        response = client.get("http://localhost:8000/api/1.0/coins/")
        # get data from db
        typemoney = TypeMoney.objects.all()
        serializer = TypeMoneySerializer(typemoney, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllTradeTest(TestCase):
    """ Test module for GET all Trades API """

    def setUp(self):
        usd = TypeMoney.objects.create(name="USD")
        eur = TypeMoney.objects.create(name="EUR")

        Trade.objects.create(sell_currency=usd, sell_amount=200, 
                             buy_currency=eur, buy_amount=206.50, rate=1.0325)
        Trade.objects.create(sell_currency=eur, sell_amount=1250.50, 
                             buy_currency=usd, buy_amount=1023.89, rate=0.9801)

    def test_get_all_trades(self):
        # get API response
        response = client.get("http://localhost:8000/api/1.0/trades/")
        # get data from db
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)   


class CreateNewTrade(TestCase):  
    """Tes module for create a new trade"""

    def setUp(self):
        usd = TypeMoney.objects.create(name="USD")
        eur = TypeMoney.objects.create(name="EUR")

        self.valid_trade = {
            "sell_currency": "USD",
            "sell_amount": "200", 
            "buy_currency": "EUR",
            "buy_amount": "206.50",
            "rate": "1.0325"
        }

        self.invalid_trade = {
            "sell_currency": " ",
            "sell_amount": "200", 
            "buy_currency": "EUR",
            "buy_amount": "206.50",
            "rate": "1.0325"
        }
        
    def test_create_valid_trade(self):
        response = client.post("http://localhost:8000/api/1.0/trades/", 
                               data=json.dumps(self.valid_trade), 
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_trade(self):
        response = client.post("http://localhost:8000/api/1.0/trades/", 
                               data=json.dumps(self.invalid_trade), 
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        




