from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Product
from .forms import ProductForm


@login_required  # decorator que protege o acesso da função por login
def product_list(request):
    products = Product.objects.all()  # recebe todos os elementos da tabela (model) Person
    print(products)
    return render(request, 'products_list.html', {'products': products})


@login_required
def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


@login_required
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)  # na tabela (model) Person procura (pk) a query id
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    # form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    # return render(request, 'person_delete_confirm.html', {'form': form})
    return render(request, 'product_delete.html', {'products': product})