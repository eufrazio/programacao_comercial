from django.views.generic import View
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, "base/index.html")

	return render(request, "acesso/login.html")