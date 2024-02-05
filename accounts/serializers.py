from rest_framework import serializers
from .models  import*


class BankStateSerializer(serializers.ModelSerializer):
    class Meta():
        model = BankState
        fields = '__all__'
        
class PhonePayReportSerializer(serializers.ModelSerializer):
    class Meta():
        model = PhonePayReports
        fields = ('PolicyNo')
        
class BankBalanceSerializer(serializers.ModelSerializer):
    class Meta():
        model = BankBalanceReports
        fields = ('PolicyNo','LedgerNo','SubLedgerNo','LGCode','TransactionDate','Narration','Amount','TenderAmount','VoucherNo')