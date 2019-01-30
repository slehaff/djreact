'train views methods'
from django.shortcuts import render
from django.http import HttpResponse


def camera(request):

    print('phone camera')
    return HttpResponse('camera view ...')

# Create your views here.
