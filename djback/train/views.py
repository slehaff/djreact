'train views methods'
from django.http import HttpResponse
from train.servers.piserve import new_receiver_thread
from train.servers.pimess import collect_mess


def collect_data(request):
    'start threads, send message to rpi3'

    folder = 'folder'
    t = new_receiver_thread('1', folder)
    collect_mess()
    t.join()

    print('collect data!')
    return HttpResponse('train view ...')

# Create your views here.
