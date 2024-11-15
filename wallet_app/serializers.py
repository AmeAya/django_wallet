from rest_framework.serializers import ModelSerializer
from .models import *


class SpendingSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['id', 'name', 'charge', 'category']
        # fields = '__all__'  # Все поля

    # to_representation -> Метод сериалайзера, который отвечает за конвертацию в JSON
    def to_representation(self, instance):
        # instance -> Джанго объект, который надо конвертировать

        # # Как примерно работает to_representation по стандарту:
        # representation = {
        #     'id': instance.id,
        #     'name': instance.name,
        #     'charge': instance.charge,
        #     'category': {
        #         'id': instance.category.id,
        #         'name': instance.category.name
        #     }
        # }
        # return representation

        representation = super().to_representation(instance)  # Использовали родной сериалайзер
        representation['category'] = {  # Переписали существующий ключ category
            'id': instance.category.id,
            'name': instance.category.name
        }

        representation['language'] = 'ru'  # Добавляем новый ключ 'language'

        representation['charge'] = representation['charge'] * 495
        return representation


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['day'] = instance.day.name
        representation['total'] = representation['price'] * representation['quantity']
        return representation
