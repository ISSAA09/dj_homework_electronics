from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify

from catalog.models import Category, Product, Blog


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Электроника- Главная'
    }
    return render(request, 'catalog/index.html', context)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = category_item.pk,
        context_data['title'] = f'{category_item.title}'

        return context_data


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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_publication=True)
        return queryset

    extra_context = {
        'title': 'Блог'
    }


class BlogCreateView(CreateView):
    model = Blog
    fields = {'title', 'description', 'creation_data', 'sign_publication','preview'}
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = {'title', 'description', 'creation_data', 'sign_publication','preview'}

    def get_success_url(self):
        return reverse_lazy('catalog:blog_detail', args=[self.object.pk])


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


# def blog_detail(request, pk):
#    category_item = Blog.objects.get(pk=pk)
#    context = {
#        'object_list': Blog.objects.filter(pk=pk),
#        'title': f'{category_item.title}'
#    }
#    return render(request, 'catalog/blog_detail.html', context)
