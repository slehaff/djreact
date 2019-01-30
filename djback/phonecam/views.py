'train views methods'
from django.shortcuts import render
from django.http import HttpResponse


def camera(request):

    print('phone camera')
    return render(request, 'camtemplate.html')
# Create your views here.
