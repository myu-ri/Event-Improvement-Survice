import pandas as pd
import os

def get_dominant_emo(df):
    # group内の要素数をカウント
    emo_counts = df['FER_dominant_emo'].value_counts()

    # 最頻値を抽出
    max_count = emo_counts.max()
    max_emos = emo_counts[emo_counts == max_count].index.tolist()

    # 最頻値が1つに決定する場合
    if len(max_emos) == 1:

        return max_emos[0]
    
    # 決定しない場合は'FER_dominant_score'を使用する
    else:
        max_emo = None
        max_score = float('-inf')
        for emo in max_emos:
            emo_scores = df.loc[df['FER_dominant_emo'] == emo, 'FER_dominant_score']
            emo_mean = emo_scores.mean()
            if emo_mean > max_score:
                max_score = emo_mean
                max_emo = emo
            
            # print('emo_scores\n', emo_scores)
            # print('emo_mean\n', emo_mean)
        
        return max_emo



def aggregate(file_name):
    # CSVファイルの読み込み
    df = pd.read_csv('./eisapp/event_Improvement_survice/detect_face_emotion/csv/' + file_name + '.csv')

    # ファイル名の文字列の取得
    df['file_name_prefix'] = df['file_name'].apply(lambda x: os.path.splitext(x)[0])

    # ファイル名の一致を検出するために長さを指定
    length = 75

    # 文字列の一致を検出
    matched = df.groupby(df['file_name_prefix'].apply(lambda x: x[:length]))

    # 同じファイルの行に対する操作
    for name, group, in matched:
        dominant_emo = get_dominant_emo(group)
        # group['dominant_emo'] = dominant_emo

        print(name)
        print(group)
        print(dominant_emo)

        print("=======================================================================================")

if __name__ == '__main__':
    name = input("イベント名を入力してください:")
    aggregate(name)