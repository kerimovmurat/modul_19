"""Проверяет данные пользователя для регистрации."""
from .models import Buyer

def valid_user(username, password, repeat_password, age):
    if password != repeat_password:
        return 'Пароли не совпадают'
    elif int(age) < 18:
        return 'Вы должны быть старше 18'
    else:
        buyers = Buyer.objects.all()
        for buyer in buyers:
            if buyer.name == username:
                return 'Пользователь уже существует'
    return None