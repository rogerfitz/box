from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	return render(request, 'admin/index.html')
