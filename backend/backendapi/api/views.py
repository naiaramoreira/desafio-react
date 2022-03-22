from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookSerializer, FoodSerializer
from .models import Book, Food


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


def insertFood(Food):
    i = 1
    while i <= 9:
        arquivo = open("../backendapi/alimentos/arquivo_0" + str(i) + ".txt", "r")
        qtd_linha =0
        for linha in arquivo:
            if qtd_linha > 1:
                item = [item for item in linha.strip('\n').split("   ") if len(item) > 0]
                food = Food(nome=item[0], quantidade=item[1], proteinas=item[2], carboidratos=item[3], gordura=item[4])
                food.save()
            qtd_linha += 1
        i +=1
        arquivo.close()
    return Food.objects.all()


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    if len(queryset) == 0:
        queryset = insertFood(Food)
    serializer_class = FoodSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]