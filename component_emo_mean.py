import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.simplefilter('ignore')
plt.style.use('ggplot')

def get_emotion_mean(df):
    # 各感情ごとの平均値を算出
    emotion_list = df[['FER[angry]', 'FER[disgust]', 'FER[fear]',
                       'FER[happy]', 'FER[sad]', 'FER[surprise]', 'FER[neutral]']]

    items = df.shape[0]
    sum_emotion = emotion_list.sum(axis = 0)
    sum_emotion = sum_emotion / items 

    return sum_emotion

def emo_mean(file_name):
    # CSVファイルの読み込み
    df = pd.read_csv('csv/' + file_name + '.csv')

    # ファイル名の文字列の取得
    df['file_name_prefix'] = df['file_name'].apply(lambda x: os.path.splitext(x)[0])

    # ファイル名の一致を検出するために長さを指定
    length = 75

    # 文字列の一致を検出
    matched = df.groupby(df['file_name_prefix'].apply(lambda x: x[:length]))

    emotion_means_list = []
    name_list = []

    # ファイル名ごとに感情の平均値を計算
    for name, group in matched:

        print(name)
        emotion_means = get_emotion_mean(group)
        print(emotion_means)

        emotion_means_list.append(emotion_means)
        name_list.append(name)
    
    num_emotions = len(emotion_means_list[0])  # 感情の数（7種類）を取得
    emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  # 感情のラベル

    # 各感情ごとに折れ線をプロット
    for i in range(num_emotions):
        values = [emotion_means[i] for emotion_means in emotion_means_list]
        plt.plot(name_list, values, marker='o', label=emotion_labels[i])

    
    max_label_length = 20 
    short_labels = [label[56:76] if len(label) > max_label_length else label for label in name_list]
    

    plt.xlabel('Name')
    plt.ylabel('Emotion Mean')
    plt.title('Average Emotion for Each File')
    plt.xticks(range(len(name_list)), short_labels, rotation=90)
    plt.legend()
    plt.tight_layout()

    plt.savefig('images/emotion_chart_' + file_name + '.jpg', dpi = 300)
    plt.show()



if __name__ == '__main__':
    name = input("イベント名を入力してください:")
    emo_mean(name)
