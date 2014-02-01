from django.shortcuts import render, redirect
from boxes.models import Box
from attr.forms import VerticalForm, TypeForm
from attr.models import Vertical, Attr, ProductType
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	a = Vertical.objects.order_by('name')
	types = ProductType.objects.order_by('name')
		
	return render(request, 'admin/attr/index.html', {'verticals': a, 'types': types})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addVertical(request):
        form = VerticalForm(request.POST)
	if request.method == 'POST':
		form.save()
		return redirect('/boxman/attrs/')
		
	return render(request, 'admin/attr/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteVertical(request, vert_id):
	Vertical.objects.get(id=vert_id).delete()
	return redirect('/boxman/attrs/')

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addType(request):
        form = TypeForm(request.POST)
	if request.method == 'POST':
		form.save()
		return redirect('/boxman/attrs/')
		
	return render(request, 'admin/attr/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteType(request, type_id):
	ProductType.objects.get(id=type_id).delete()
	return redirect('/boxman/attrs/')
