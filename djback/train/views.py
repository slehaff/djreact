'train views methods'
from django.http import HttpResponse


def collect_data(request):
    'start threads, send message to rpi3'
    print('collect data!')
    return HttpResponse('train view ...')

# Create your views here.
