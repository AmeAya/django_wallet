from rest_framework.serializers import ModelSerializer
from .models import *


class SpendingSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['id', 'name', 'charge', 'category']
        # fields = '__all__'  # Все поля
