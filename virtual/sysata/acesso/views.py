from django.views.generic import View
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class LoginView(View):

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, 'base/index.html' )
		return render(request, 'acesso/login.html', { })


	def post(self, request):
		# username = request.POST['username']
		username = request.POST.get('username')
		# password = request.POST['password']
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return render(request, "base/index.html")
		else:
			return render(request, "acesso/login.html")
			#return HttpResponse("Usuario ou senha invalidos!")

		# return render(request, "base/index.html")

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(settings.LOGIN_URL)