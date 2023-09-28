from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Электроника- Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Электроника- наша жизнь!'
    }
    return render(request, 'catalog/categories.html', context)


def electronic_category(request,pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/electronics.html', context)

# def contacts(request):
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
#    return render(request, 'catalog/contacts.html')
