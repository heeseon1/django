from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import AddProductForm
from shop.forms import ReviewForm
from django.views.generic.edit import CreateView

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category': current_category, 'categories': categories, 'products': products})


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    reviews = Review.objects.filter(product=product).all()
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart': add_to_cart, 'reviews':reviews})



def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
        return redirect('/')
    else:
        form = ReviewForm()
    return render(request, 'shop/review_create.html', {'form':form})

def review_delete(request,review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

