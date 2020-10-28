from PIL import Image
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from .forms import Product, ProductForm, Category, CategoryForm, WorkForceRegistrationForm


# Create your views here.


class Home(ListView):
    model = Category
    queryset = Category.objects.all().filter(active=True)
    template_name = 'home-&-about/home.html'


class About(TemplateView):
    template_name = 'home-&-about/about.html'


class Dashboard(TemplateView):
    template_name = 'dashboard.html'


class ProdList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Product
    template_name = 'CRUD/product/retrieve/list_view.html'


class ProdDetail(DetailView):
    model = Product
    template_name = 'CRUD/product/retrieve/detail_view.html'


class ProdCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = ProductForm
    model = Product
    extra_context = {
        'title': 'Add Product',
        'var': 'Add',
    }
    template_name = 'CRUD/product/create.html'
    success_url = reverse_lazy('create_product')


class ProdUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = ProductForm
    model = Product
    extra_context = {
        'title': 'Update Product',
        'var': 'Update',
    }
    template_name = 'CRUD/product/update.html'
    success_url = reverse_lazy('list_product')


class ProdDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Product
    extra_context = {
        'title': 'Delete Product',
        'var': 'Delete',
    }
    template_name = 'CRUD/product/delete.html'
    success_url = reverse_lazy('list_product')


class CatList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Category
    template_name = 'CRUD/category/retrieve/list_view.html'


def CatDetail(request, slug):
    object_list = Product.objects.all().filter(category__slug=slug, active=True)
    for i in object_list:
        if i.image_1:
            pic = '.' + i.image_1.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
        if i.image_2:
            pic = '.' + i.image_2.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
        if i.image_3:
            pic = '.' + i.image_3.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
        if i.image_4:
            pic = '.' + i.image_4.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
        if i.image_5:
            pic = '.' + i.image_5.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
        if i.image_6:
            pic = '.' + i.image_6.url
            image = Image.open(pic)
            if image.size != (1080, 480):
                new_size = (1080, 480)
                new = image.resize(new_size)
                new.save(pic)
            else:
                pass
    context = {
        'object_list': object_list,
    }
    return render(request, template_name='CRUD/category/retrieve/detail_view.html', context=context)


class CatCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CategoryForm
    model = Category
    extra_context = {
        'title': 'Add Category',
        'var': 'Add',
    }
    template_name = 'CRUD/category/create.html'
    success_url = reverse_lazy('create_category')


class CatUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CategoryForm
    model = Category
    extra_context = {
        'var': 'Update',
        'title': 'Update Category',
    }
    template_name = 'CRUD/category/update.html'
    success_url = reverse_lazy('list_category')


class CatDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Category
    extra_context = {
        'title': 'Delete Category',
        'var': 'Delete',
    }
    template_name = 'CRUD/category/delete.html'
    success_url = reverse_lazy('list_category')


class create_workforce(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = WorkForceRegistrationForm
    model = User
    template_name = 'CRUD/workforce/create.html'
    extra_context = {
        'var': 'Submit',
        'title': 'Workforce Registration',
    }
    success_url = reverse_lazy('dashboard')


class delete_workforce(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'CRUD/workforce/delete.html'
    extra_context = {
        'var': 'Delete',
        'title': 'Delete Workforce',
    }
    success_url = reverse_lazy('workforce_list')


class update_workforce(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    fields = {
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_superuser',
    }
    extra_context = {
        'var': 'Update',
        'title': 'Update Workforce',
    }
    template_name = 'CRUD/workforce/update.html'
    success_url = reverse_lazy('workforce_list')


class workforce_list(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = User
    queryset = User.objects.all().filter(is_staff=True, is_superuser=False)
    template_name = 'CRUD/workforce/retrieve/list_view.html'


class workforce_detail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'CRUD/workforce/retrieve/detail_view.html'


@login_required(login_url=reverse_lazy('login'))
def change_password(request):  # Tested and PWNE
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'title': 'Change Password',
        'var': 'Change',
    }
    return render(request, template_name='registration/change_password.html', context=context)
