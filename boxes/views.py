from django.shortcuts import render, redirect
from boxes.models import Box
from boxes.forms import BoxForm
from products.models import Product
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	boxes= Box.objects.order_by('price')#.distinct('price')Doesn't work in mysql
	for box in boxes:
		products = box.products.all()

	bz = []
	for box in boxes:
		b = Box()
		b.product=box.products.all()
		b.id=box.id
		bz.append(b)
	return render(request, 'admin/boxes/boxes.html', {'boxes': boxes})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addBox(request):
	products= Product.objects.all()
	if request.method == 'POST':
		box=Box()
		products = []
		box.price = 0.0
		for product_id in request.POST.getlist('id'):
			p = Product.objects.get(id=int(product_id))
			box.price += float(p.price)
			products.append(p)
		box.save()

		for p in products:
			box.products.add(p)
		
		return redirect('/boxman/boxes/')
	return render(request, 'admin/boxes/products.html', {'products': products})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteBox(request, box_id):
	Box.objects.get(id=box_id).delete()
	return redirect('/boxman/boxes/')
