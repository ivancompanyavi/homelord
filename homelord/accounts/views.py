from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from accounts.forms import UserForm


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            user = uf.save()
            return HttpResponseRedirect('main')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'form': uf}, RequestContext(request))
