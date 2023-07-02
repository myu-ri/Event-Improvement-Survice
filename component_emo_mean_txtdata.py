import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.simplefilter('ignore')
plt.style.use('ggplot')

def get_emotion_mean_txtdata(df):
    # 各感情ごとの平均値を算出
    emotion_list = df[['FER[angry]', 'FER[disgust]', 'FER[fear]',
                       'FER[happy]', 'FER[sad]', 'FER[surprise]', 'FER[neutral]']]

    items = df.shape[0]
    sum_emotion = emotion_list.sum(axis = 0)
    sum_emotion = sum_emotion / items 

    return sum_emotion

def emo_mean_txtdata(file_name):
    # CSVファイルの読み込み
    df = pd.read_csv('./eisapp/event_Improvement_survice/detect_face_emotion/csv/' + file_name + '.csv')

    # ファイル名の文字列の取得
    df['file_name_prefix'] = df['file_name'].apply(lambda x: os.path.splitext(x)[0])

    # ファイル名の一致を検出するために長さを指定
    length = 128

    # 文字列の一致を検出
    matched = df.groupby(df['file_name_prefix'].apply(lambda x: x[:length]))

    emotion_means_list = []
    name_list = []
    # emotion_means_listを辞書のリストに変換する（Django出力用）
    emotion_means_dict_list = []

    # ファイル名ごとに感情の平均値を計算
    for name, group in matched:

        print(name)
        emotion_means = get_emotion_mean_txtdata(group)
        print(emotion_means)

        emotion_means_list.append(emotion_means)
        name_list.append(name)
    
    for emotion_means in emotion_means_list:
        emotion_means_dict = emotion_means.to_dict()
        emotion_means_dict_list.append(emotion_means_dict)
    
    num_emotions = len(emotion_means_list[0])  # 感情の数（7種類）を取得
    emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  # 感情のラベル

    # emotion_means_listを辞書のリストに変換する
    emotion_means_dict_list = []
    for emotion_means in emotion_means_list:
        emotion_means_dict = emotion_means.to_dict()
        emotion_means_dict_list.append(emotion_means_dict)

    return emotion_means_dict_list, name_list

