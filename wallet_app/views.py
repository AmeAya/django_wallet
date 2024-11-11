from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class TestApiView(APIView):
    permission_classes = [AllowAny]
    # permission_classes -> Доступы, кто может пользоваться этим АПИ
    # IsAuthenticated - Только авторизованные пользователи
    # IsAdminUser - Только админы(is_staff равно True)
    # AllowAny - Доступ есть у всех

    # GET -> ГЕТ запросы используются для "получения" данных
    def get(self, request):  # Функция, которая будет вызвана когда к нам придет ГЕТ запрос
        return Response(data={'message': 'Hello, World!'}, status=status.HTTP_200_OK)


class SpendingApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        spendings = Spending.objects.all()  # Берем все записи из таблицы Spending
        # spendings -> Все записи имеют тип данных QuerySet(Джанго сет)
        # Чтобы конвертировать из Джанго объекта в JSON используются сериалайзеры
        # Сериализация - Процесс, конвертации данных в установленный формат(Обычно JSON)

        data = SpendingSerializer(instance=spendings, many=True).data
        # instance -> Джанго объект(-ы), который хотим конвертировать
        # many -> True, если в instance несколько объектов. Если один, то False

        return Response(data=data, status=status.HTTP_200_OK)
