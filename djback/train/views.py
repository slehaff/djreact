'train views methods'
from django.http import HttpResponse


def collect_data(request):
    print('collect data!')
    return HttpResponse('train view ...')

# Create your views here.
