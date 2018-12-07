import socket
import camin as cm
import gamma as gm


IP = '0.0.0.0'
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, port))
i = 1
while i == 1:
    data, addr = sock.recvfrom(1024)
    if data == 'quit':
        i = 0
        break
    elif data == 'procal':
        cm.capt_pro_cos(cfolder=data)
    elif data == 'cam_cal':
        cm.cam_cal(data)
        print('calibrate')
    elif data == '3cos':
        cm.capture3cos(data)
    elif data == '3singlecos':
        cm.capture3cos(data)
    elif data == 'wilm_cal':
        cm.wilm_cal(data)
    elif data == 'scan':
        print('scan start')
        cm.scan(data)
    elif data == '4cos':
        cm.scan4(data)
    elif data == 'abs_scan':
        cm.abs_scan(data)
    elif data == 'gamma_scan':
        gm.gamma_cal()

    print('Received:', data)
