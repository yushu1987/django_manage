from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'login.html')
#    return HttpResponse('Hello World')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username', '')
        passwd = request.POST.get('password', '')
        if uname == 'wangjian' and passwd == '123456':
            return HttpResponse('login success')
        else:
            ret = {}
            ret['error'] = 'invalid username or password'
            return render(request, 'login.html', ret)
    else:
        raise Exception('invalid method')

