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

    def post(self, request):  # POST -> Для создания нового spending
        # Данные лежат в теле запроса(Body) -> request.data
        # print(request.data)
        #
        # spending_name = request.data.get('name')  # Берем только name из тела запроса
        # spending_name = request.data.get('title')  # Пытаемся взять title, которого нет(None)
        # print(spending_name)
        # get('<KEY>') -> Если ключа <KEY> не было в теле запроса, то Джанго вернет None

        new_spending = SpendingSerializer(data=request.data)
        if new_spending.is_valid():
            # .is_valid() -> Метод сериалайзера, который проверяет все ли поля в request.data
            #                соответствуют полям в модельке и правильный ли у них тип данных
            new_spending.save()  # .save() -> Метод сериалайзера, который сохраняет(создает) запись в БД
            return Response(data={'message': 'Spending Created!'}, status=status.HTTP_200_OK)
        else:
            # print(new_spending.errors)
            # .errors -> Метод сериалайзера, возвращающий ошибки которые у него возникли в формате dict
            return Response(data=new_spending.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):  # PATCH -> Для обновления уже существующего spending
        spending = Spending.objects.get(id=request.data.get('id'))
        updated_spending = SpendingSerializer(instance=spending, data=request.data, partial=True)
        # partial -> Если стоит True, то сериалайзер обновляет только те поля, которые смог найти в request.data
        #            Иначе, если стоит False, то сериалайзер обновляет все поля и будет искать их в request.data
        if updated_spending.is_valid():
            updated_spending.save()
            return Response(data={'message': 'Spending Updated!'}, status=status.HTTP_200_OK)
        else:
            return Response(data=updated_spending.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):  # DELETE -> Для удаления уже существующего spending
        spending = Spending.objects.get(id=request.data.get('id'))
        spending.delete()  # .delete() -> Метод моделек, который удаляет запись из БД
        return Response(data={'message': 'Spending Deleted!'}, status=status.HTTP_200_OK)


# 1) Создать новую модель Income(name -> CharField, charge -> IntegerField)
# 2) Для модели Income создать IncomeSerializer
# 3) Создать вью IncomeApiView в которой нужно реализовать запросы:
# 3.1. GET -> Вернуть все записи из Income
# 3.2. POST -> Создать новый Income
# 3.3. PATCH -> Обновить существующий Income по id
# 3.4. DELETE -> Удалить существующий Income по id
