#from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
#from example_project.models import Order

#class OrderSerializer(DocumentSerializer):
  #class Meta:
    #model = Order
    #fields = '__all__'


from images.models import Images
#from images.models import Stock6Sign202212, Stock6Sign202304, Stock6Sign202308, Stock6Sign202309, Stock6Sign202310, Stock6Sign202311, Stock6Sign202312, Stock6Sign202402
from images.models import  Stock6Sign202212, Stock6Sign202304, Stock6Sign202308, Stock6Sign202309, Stock6Sign202310, Stock6Sign202311, Stock6Sign202312, Stock6Sign202402,Stock6Sign202403,Stock6Sign202404,Stock6Sign202405,Stock6Sign202406,Stock6Sign202407,Stock6Sign202408,Stock6Sign202409,Stock6Sign202410,Stock6Sign202411,Stock6Sign202412


class ImageSerializer(DocumentSerializer):
    class Meta:
        model = Images
        # fields = '__all__'
        #fields = ('id', 'Url', 'CreateDate')
        fields = '__all__'
class Stock6Sign202212Serializer(DocumentSerializer):
    class Meta:

        model = Stock6Sign202212
        # fields = '__all__'
        #fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate')
        fields = '__all__'
class Stock6Sign202304Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202304
        # fields = '__all__'
        #fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate', 'cRevN', 'cRev','ca1N','ca2N','ca3N','ca4N','ca5N', 'ca6N','ca7N', 'cna1','cna2','cna3','cna4','cna5','cna6', 'cna7','cna9','cna10','cnewest_Rev_month','cluX','cnluX_MoM','cProfitN','cProfit','cb1N','cb2N','cb3N','cb4N','cb5N','cb6N','cb7N','cb8N','cb1','cb2','cb3','cb4','cb5','cb6', 'cb7','cb8','cb9',  'cb10','cb10p','cInvTON','cInvTO','ce1N','ce2N','ce3N','ce4N','ce5N','ce6N','ce7N','ce8N','ce1','ce2','ce3','ce4','ce5','ce6','ce7','ce8','cnewest_Fin_Q','cNetIncomeN','cNetIncome','cc1N','cc2N','cc3N','cc4N','cc5N','cc6N', 'cc7N','cc8N','cc1','cc2','cc3','cc4','cc5','cc6','cc7', 'cc8', 'cc9',  'cc10','cc11','cpc9', 'cpc10','cpc11','cEPSN','cEPS','cd1N','cd2N','cd3N','cd4N','cd5N','cd6N','cd7N','cd8N','cd1','cd2','cd3','cd4','cd5','cd6','cd7','cd8','cCashFlowN','cCashFlow','cf1N','cf2N','cf3N','cf4N','cf5N','cf6N','cf7N','cf8N','cf1','cf2','cf3','cf4','cf5','cf6','cf7','cf8', 'cf9','cf10')
        fields = '__all__'
class Stock6Sign202308Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202308
        # fields = '__all__'
        #fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate', 'cRevN', 'cRev','ca1N','ca2N','ca3N','ca4N','ca5N', 'ca6N','ca7N', 'cna1','cna2','cna3','cna4','cna5','cna6', 'cna7','cna9','cna10','cnewest_Rev_month','cluX','cnluX_MoM','cProfitN','cProfit','cb1N','cb2N','cb3N','cb4N','cb5N','cb6N','cb7N','cb8N','cb1','cb2','cb3','cb4','cb5','cb6', 'cb7','cb8','cb9',  'cb10','cb10p','cInvTON','cInvTO','ce1N','ce2N','ce3N','ce4N','ce5N','ce6N','ce7N','ce8N','ce1','ce2','ce3','ce4','ce5','ce6','ce7','ce8','cnewest_Fin_Q','cNetIncomeN','cNetIncome','cc1N','cc2N','cc3N','cc4N','cc5N','cc6N', 'cc7N','cc8N','cc1','cc2','cc3','cc4','cc5','cc6','cc7', 'cc8', 'cc9',  'cc10','cc11','cpc9', 'cpc10','cpc11','cEPSN','cEPS','cd1N','cd2N','cd3N','cd4N','cd5N','cd6N','cd7N','cd8N','cd1','cd2','cd3','cd4','cd5','cd6','cd7','cd8','cCashFlowN','cCashFlow','cf1N','cf2N','cf3N','cf4N','cf5N','cf6N','cf7N','cf8N','cf1','cf2','cf3','cf4','cf5','cf6','cf7','cf8', 'cf9','cf10')
        fields = '__all__'
class Stock6Sign202309Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202309
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202310Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202310
        # fields = '__all__'
        fields = '__all__'

class Stock6Sign202311Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202311
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202312Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202312
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202402Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202402
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202403Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202403
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202404Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202404
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202405Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202405
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202406Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202406
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202407Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202407
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202408Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202408
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202409Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202409
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202410Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202410
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202411Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202411
        # fields = '__all__'
        fields = '__all__'
class Stock6Sign202412Serializer(DocumentSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202412
        # fields = '__all__'
        fields = '__all__'