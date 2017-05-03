from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def index(request):

    return render_to_response('base/index.html', )

# class IndexView(View):

# 	def index(self, request):
# 		return render(request, 'base/index.html' )