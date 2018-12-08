'rpi3 server receiver'

import socket
import struct
import threading
import shutil
import os
import numpy as np
import cv2


def mov_files(dir_to):
    'Docstring'
    path = '/home/samir/djreact/djback/train/static/im_folder/'
    moveto = dir_to
    files = os.listdir(path)
    files.sort()
    for f in files:
        src = path + f
        dst = moveto + f
        shutil.move(src, dst)


def rcv_all(sock, count):
    'Doctring'
    buf = b''
    while count:
        new_buf = sock.recv(count)
        if not new_buf:
            return None
        buf += new_buf
        count -= len(new_buf)
    return buf


def new_receiver_thread(folder):
    'Docstring'
    t = threading.Thread(target=new_receive_pi_data,
                         args=(folder, ),
                         name='T1')
    t.start()
    return t


def new_receive_pi_data(to_folder):
    'Docstring'
    print('new receive called')
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8001))
    server_socket.listen(0)
    conn, _ = server_socket.accept()
    i = 0
    try:
        while True:
            image_len = struct.unpack(
                '<L', conn.recv(struct.calcsize('<L')))[0]
            if not image_len:
                break
            string_data = rcv_all(conn, int(image_len))
            data = np.fromstring(string_data, dtype='uint8')
            dec_img = cv2.imdecode(data, 1)
            dec_img = cv2.flip(dec_img, 1)  # Invert image
            dec_img = cv2.flip(dec_img, -1)  # Invert image
            dec_img = cv2.flip(dec_img, 0)  # Invert image
            print('received image!')
            # dec_img = dec_img[25:265, 180:630]
            i += 1
            folder = '/home/samir/djreact/djback/train/static/im_folder/'
            cv2.imwrite(folder + '/image' + str(i)+'.png', dec_img)
            print('i=', i, image_len, dec_img.shape)
    finally:
        conn.close()
        server_socket.close()
        mov_files(to_folder)
        print('closed')
