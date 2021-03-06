from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductForm, FullProductForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	products= Product.objects.order_by('price')
	
	return render(request, 'admin/products/products.html', {'products': products})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addProduct(request):
	form = ProductForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			print request.POST
			product = form.save(commit=False)
			product.price_per_box = float(request.POST['price'])*float(request.POST['items_in_box'])/float(request.POST['items_per_purchase'])
			try:
				p = Product.objects.get(name=product.name)
				if p.items_per_box != product.items_per_box:
					product.save()
				else:
					print product.name+' already exists'
			except:
				product.save()
		
			return redirect('/boxman/products/')

	return render(request, 'admin/products/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def editProduct(request, product_id):
	product = Product.objects.get(id=product_id)
	form = FullProductForm(instance=product)

	if request.method == 'POST':
		form = FullProductForm(request.POST, instance=product)
		if form.is_valid():		
			product.price_per_box = product.price*product.items_in_box/product.items_per_purchase
			form.save()
			return redirect('/boxman/products/')

	return render(request, 'admin/products/add.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteProduct(request, product_id):
	Product.objects.get(id=product_id).delete()
	return redirect('/boxman/products/')

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def purchaseProduct(request, product_id):
	product = Product.objects.get(id=product_id)
	product.item_count+=product.items_per_purchase
	product.save()
	return redirect('/boxman/products/')

