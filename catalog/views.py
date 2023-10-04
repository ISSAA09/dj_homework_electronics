from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.models import Category, Product, Blog


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Электроника- Главная'
    }
    return render(request, 'catalog/index.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Электроника - Территория низких цен!'
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'{category_item.name}'

        return context_data


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Введение блога!'
    }


class BlogCreateView(CreateView):
    model = Blog
    fields = {'title', 'description', 'creation_data', 'sign_publication'}
    success_url = reverse_lazy('catalog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = {'title', 'description', 'creation_data', 'sign_publication'}
    success_url = reverse_lazy('catalog:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')

# def categories(request):
#    context = {
#        'object_list': Category.objects.all(),
#        'title': 'Электроника - Территория низких цен!'
#    }
#    return render(request, 'catalog/category_list.html', context)


# def electronic_category(request, pk):
#    category_item = Category.objects.get(pk=pk)
#    context = {
#        'object_list': Product.objects.filter(category_id=pk),
#        'title': f'{category_item.name}'
#    }
#    return render(request, 'catalog/product_list.html', context)

# def contacts(request):
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
#    return render(request, 'catalog/contacts.html')
