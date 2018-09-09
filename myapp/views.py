from django.shortcuts import render, redirect
from .forms import ConditionForm, CityForm
from .models import Condition
from .utils import get_weather_data, get_arranged_data
from django.http import HttpResponse
from django.contrib import messages
import requests
# Create your views here.

# def register_condition(request):
# 	if request.method == 'POST':
# 		form = ConditionForm(request.POST or None)
# 		if form.is_valid():
# 			ins = form.save(commit=False)
# 			ins.save()
# 			return HttpResponse('Register Success')
# 	else:
# 		form = ConditionForm()
# 	context = {'form': form, }
# 	return render(request, 'register.html', context)

def get_weather(request):
	if request.method == 'POST':
		form = CityForm(request.POST or None)
		if form.is_valid():
			city_name = form.cleaned_data['city']
			xList = get_weather_data(city_name)
			if xList != 0:
				context = get_arranged_data(xList)
				query = Condition.objects.get(spl_code=context['curr_weather_code'])
				context.update({'query': query, 'form': form, })
				return render(request, 'sample.html', context)
			else:
				# messages.error(request, "Location Undetermined. Please enter a proper city.")
				return HttpResponse('<h2>Location Undetermined. Please Enter a proper city.</h2>')
				# return redirect('get_weather')
	else:
		form = CityForm()
		data = requests.get('http://ip-api.com/json').json()
		if data['status'] != 'success':
			return HttpResponse('<h3>Failed</h3>')
		city_name = data['city']
		xList = get_weather_data(city_name)
		if xList != 0:
			context = get_arranged_data(xList)
			query = Condition.objects.get(spl_code=context['curr_weather_code'])
			context.update({'query': query, 'form': form, })
			return render(request, 'sample.html', context)
		else:
			return HttpResponse('<h2>Location Undetermined. Please Enter a proper city.</h2>')


# def home(request):
# 	data = requests.get('http://ip-api.com/json').json()
# 	if data['status'] != 'success':
# 		return HttpResponse('<h3>Failed</h3>')
# 	city_name = data['city'];
# 	xList = get_weather_data(city_name)
# 	if xList != 0:
# 		context = get_arranged_data(xList)
# 		query = Condition.objects.get(spl_code=context['curr_weather_code'])
# 		context.update({'query': query, })
# 		return render(request, 'sample.html', context)
