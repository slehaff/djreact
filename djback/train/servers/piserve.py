'rpi3 server receiver'

import socket
import cv2
import numpy as np
import struct
import threading
import shutil
import os


def new_receiver_thread(n, folder):
    t = threading.Thread(target=new_receive_pi_data,
                         args=(n, folder),
                         name='T1')
    t.start()
    return t


def new_receive_pi_data(n, to_folder):
    print('new receive called')
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8001))
    server_socket.listen(0)
    conn, adr = server_socket.accept()
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
            folder = '/home/samir/PycharmProjects/danbotsIII/scan/static/scan_folder/im_folder'
            cv2.imwrite(folder + '/image' + str(i)+'.png', dec_img)
            print('i=', i, image_len, dec_img.shape)
    finally:
        conn.close()
        server_socket.close()
        mov_files(to_folder)
        print('closed')
