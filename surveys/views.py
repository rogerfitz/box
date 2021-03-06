from django.shortcuts import render, redirect
from surveys.models import ProductSurvey, BoxSurvey
from surveys.forms import ProductSurveyForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	surveys = ProductSurvey.objects.all()
	return render(request, 'admin/surveys/list.html', {'surveys': surveys})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def createSurvey(request):
	if request.method == 'POST':
		form = ProductSurveyForm(request.POST)
		form.save()
		return redirect('/surveys/')
	else:
		form = ProductSurveyForm()

	return render(request, 'admin/surveys/add.html', {'form': form})
'''
def deleteSurvey(request, survey_id):
	Box.objects.get(id=survey_id).delete()
	return redirect('/boxes/')
'''
