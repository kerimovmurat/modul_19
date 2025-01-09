from django.template.context_processors import request
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .tools import valid_user
from .models import Buyer, Game, News


# Create your views here.
def menu(request):
    title_m = 'Главная страница'
    main = 'Главная'
    shop = 'Магазин'
    basket = 'Корзина'
    new = 'Новости'

    context = {
        'title': title_m,
        'main': main,
        'shop': shop,
        'basket': basket,
        'new': new,
    }
    return render(request, 'fourth_task/index.html', context)


def play(request):
    title_s = 'Игры'
    main = 'Главная'
    shop = 'Магазин'
    basket = 'Корзина'
    back = 'Вернуться обратно'
    games = Game.objects.all()
    context = {
        'title': title_s,
        'list': games,
        'main': main,
        'shop': shop,
        'basket': basket,
        'back': back,
    }
    return render(request, 'fourth_task/index2.html', context)

class Cart(TemplateView):
    template_name = 'fourth_task/index3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['message'] = 'Извините ваша корзина пуста'
        context['back'] = 'Вернуться обратно'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['basket'] = 'Корзина'
        return context

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            error = valid_user(username, password, repeat_password, age)
            if error:
                form.add_error(None, error)
            else:
                Buyer.objects.create(name=username, balance=100, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = valid_user(username, password, repeat_password, age)
        if error:
            info['error'] = error
        else:
            Buyer.objects.create(name=username, balance=100, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', context=info)

def page(request):
    posts = News.objects.all().order_by('date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context = {
        'news': news,
    }
    return render(request, 'news.html', context)