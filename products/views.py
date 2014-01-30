from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	products= Product.objects.order_by('name')
	return render(request, 'admin/products/products.html', {'products': products})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addProduct(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		product = form.save(commit=False)
		try:
			p = Product.objects.get(name=product.name)
			if p.items_per_box != product.items_per_box:
				product.save()
		except:
			product.save()
		
		return redirect('/products/')
	else:
		form = ProductForm()

	return render(request, 'admin/products/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteProduct(request, product_id):
	Product.objects.get(id=product_id).delete()
	return redirect('/products/')

