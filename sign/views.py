from django.http import HttpResponse
from django.shortcuts import render
import json
from sign.service.user_service import UserService

# Create your views here.

def index(request):
    return render(request, 'login.html')

def api_response(request):
    data_dict = {'username': 'wangjian', 'password' : ''}
    response_dict = {'error': 0, 'msg' : 'success', 'data':data_dict}
    return HttpResponse(json.dumps(response_dict))

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

def get_user_list(request):
    userService = UserService(0)
    user_list = userService.get_all_user()
    return render(request,'guest.html',{'user_list': user_list})

