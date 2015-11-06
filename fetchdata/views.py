
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.dispatch import receiver
from django.db import models
from django.db.models import F, Q
from django.core.files.storage import default_storage as storage

from fetchdata.models import Tweet

from fetchdata.forms import keyword

def add(request):
	if request.method == 'POST':
		form = keyword(request.POST)
		if form.is_valid():
			print form.cleaned_data['word']
			msg = 'keyword is  : ', form.cleaned_data['word']
			# Call the script function
			return render (request, 'add.html', locals() )
	else:
		form = keyword()
	
		return render (request, 'add.html', locals() )


