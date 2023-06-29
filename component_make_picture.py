import cv2
import os
import datetime
import numpy as np

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return


    n = 0

    #stime = ''
    #etime = ''
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        # Enterを押した際に終了
        if cv2.waitKey(1) == 13:
            break
        if n == cycle:
            n = 0

            date = datetime.datetime.now()
            now = date.strftime('%Y-%m-%d_%H-%M-%S')
            os.makedirs(dir_path, exist_ok=True)
            base_path = os.path.join(dir_path, basename)

            # ファイル保存
            imwrite('{}_{}.{}'.format(base_path, now, ext), frame)

        n += 1

    #etime = date.time().strftime('%H-%M-%S')
    #time = stime + '~' + etime

    cv2.destroyWindow(window_name)

    #return day

# FPSを参照
# cycle = 300 : 10s
if __name__ == '__main__':
    name = input("イベント名を入力してください:")
    save_frame_camera_cycle(0, 'data/' + name, 'camera_capture_cycle', 150)