from django.http import HttpResponse
from shortcuts import redirect
def index(request):
	return HttpResponse("okla")
def re(request):
	return redirect('/index')