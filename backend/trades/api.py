import requests
from decimal import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import status
from .models import Trade, TypeMoney
from .serializers import TradeSerializer, TypeMoneySerializer, CurrenciesSerializer, RateSerializer


class TradeViewSet(ModelViewSet):
    """ Trade Viewset with set of HTTP Methods

        list[GET]: return all trades. 
        create[POST]: create one trade.
        retrieve[GET]: get a trade with his pk 
        update[PUT]: update a trade
        partial_update[PATCH]: update some attributes of a trade 
        destroy[DELETE]: delete the trade selected 
        getRate[GET]: get a rate with two currencies     
    """
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    
    def perform_create(self, serializer):
       
        sell_currency = serializer.validated_data['sell_currency']
        buy_currency = serializer.validated_data['buy_currency']
        serializer.validated_data['rate'] = self.rateRequest(
                                                            sell_currency.name, 
                                                            buy_currency.name)
        sell_amount = serializer.validated_data['sell_amount']
        serializer.validated_data[
            'buy_amount'] = sell_amount * Decimal(serializer.validated_data[
                                                                    'rate'])
        serializer.save()
            

    @list_route(methods=['get'])
    def getRate(self, request, pk=None):
        """ 
        Get rate
        :param request: HttpRequest, sell_currency: string, 
               buy_currency: string
        :return Response
        """
    
        currencies_serialiser = CurrenciesSerializer(
                                    data=self.request.query_params)

        currencies_serialiser.is_valid(raise_exception=True)

        sell_currency = currencies_serialiser.validated_data['sell_currency']
        buy_currency = currencies_serialiser.validated_data['buy_currency']

        return Response({
            'rate': self.rateRequest(sell_currency, buy_currency)
        })

    def rateRequest(self, sell_currency, buy_currency):
        currencies = {'base': sell_currency, 'symbols': buy_currency}
        rate_request = requests.get("http://api.fixer.io/latest", 
                                    currencies)

        rate_serializer = RateSerializer(data=rate_request.json())
        rate_serializer.is_valid(raise_exception=True)
        
        return rate_serializer.validated_data['rates'][buy_currency]
        

class TypeMoneyViewSet(ModelViewSet):
    """ TypeMoney Viewset with set of HTTP Methods

        list[GET]: return all type of moneys. 
        create[POST]: create one type of money.
        retrieve[GET]: get a type of money 
        update[PUT]: update a type of money 
        destroy[DELETE]: delete one type of money    
    """
    queryset = TypeMoney.objects.all()
    serializer_class = TypeMoneySerializer
