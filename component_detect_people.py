from ultralytics import YOLO
import glob
import pandas as pd
from ultralytics import YOLO
import torch
import numpy as np
import warnings
import datetime

warnings.simplefilter('ignore')

def detect_people(name):
    # モデルの生成
    model = YOLO("yolov8s.pt")

    # 参照画像
    img_files = glob.glob("./eisapp/event_Improvement_survice/detect_face_emotion/data/" + name + "/*.jpg")
    # 保存先
    files = "./eisapp/event_Improvement_survice/detect_face_emotion/runs/detect/"

    # 推論実行
    # save=True: 画像保存
    # save_txt: 検出結果をテキスト保存（ラベル・座標）
    # save_conf: 各物体のconfidence（スコア）
    # save_crop = True: 検出した物体を切り出し
    # results = model("data/camera_capture_cycle_2023-04-20,15-19-17.jpg")
    results = model.predict(source=img_files, #参照画像
                            project=files, #保存先
                            name="predict", #保存するフォルダ名
                            save_txt = True,
                            save_conf = True,
                            save = True, conf = 0.8,
                            classes = [0],
                            save_crop = True)

    #labels = glob.glob("./runs/detect/predict/labels/*.txt")

    """
    df = pd.DataFrame()
    
    for i in labels:
        # CSV出力
        df = df.append(pd.read_csv(i, sep = ' ', header=None, names=['id', 'x1', 'y1', 'x2', 'y2', 'score']))

        # tensor
        img_data = np.array(pd.read_csv(i, sep = ' ', header=None, names=['id', 'x1', 'y1', 'x2', 'y2', 'score']))
        img_data = torch.from_numpy(img_data)
    
    print(df)
    """

if __name__ == '__main__':
    name = input("イベント名を入力してください:")
    detect_people(name)