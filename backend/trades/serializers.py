from rest_framework import serializers
from .models import Trade, TypeMoney


class TypeMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMoney
        fields = '__all__'


class TradeSerializer (serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = (
            'sell_currency', 'sell_amount', 'buy_currency', 
            'buy_amount', 'rate', 'date_booked')


class CurrenciesSerializer (serializers.Serializer):
    sell_currency = serializers.CharField(max_length=3, min_length=3,
                                          required=True)
    buy_currency = serializers.CharField(max_length=3, min_length=3, 
                                         required=True)

    def validate_sell_currency(self, data):
        if data != data.upper():
            raise serializers.ValidationError("should be written in capital" + 
                                              "letters")
        return data

    def validate_buy_currency(self, data):
        if data != data.upper():
            raise serializers.ValidationError("should be written in capital" + 
                                              "letters")
        return data


class RateSerializer (serializers.Serializer):
    rates = serializers.JSONField()







