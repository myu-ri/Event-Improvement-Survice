from fer import FER
from deepface import DeepFace
import matplotlib.pyplot as plt
import glob
import csv
import os

def detect_emo(name):
    image_file = glob.glob('./eisapp/event_Improvement_survice/detect_face_emotion/runs/detect/predict/crops/person/*.jpg')

    os.makedirs("./eisapp/event_Improvement_survice/detect_face_emotion/csv", exist_ok=True)

    # CSVファイル作成
    with open('./eisapp/event_Improvement_survice/detect_face_emotion/csv/' + name + '.csv', 'w', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(['file_name', 'FER_dominant_emo', 'FER_dominant_score', 'DF_dominant_emo', 'DF_dominant_score'])
        writer.writerow(['file_name', 'FER_dominant_emo', 'FER_dominant_score', 
                         'FER[angry]', 'FER[disgust]', 'FER[fear]',
                         'FER[happy]', 'FER[sad]', 'FER[surprise]', 'FER[neutral]'])
    
        for i in image_file:
            images = plt.imread(i)  

            # FER
            emo_detector = FER(mtcnn=True)
            captured_emo_FER = emo_detector.detect_emotions(images)
            print("FER_Emo_list: ", i, "\n", captured_emo_FER)
            if captured_emo_FER and captured_emo_FER[0]['emotions']:
                print("FER_Emo_list[emotion]: ", i, "\n", captured_emo_FER[0]['emotions'])
            else:
                continue
            dominant_emo_FER, emo_score = emo_detector.top_emotion(images)
            print("FER_dominant_Emo: ", i, "\n", dominant_emo_FER, emo_score)

            # DeepFace
            captured_emo_DF = DeepFace.analyze(images, actions=['emotion'], enforce_detection=False)
            # print('DeepFace: ', i, "\n", captured_emo_DF)

            # crop画像の描画
            # plt.imshow(images)
            # plt.show()

            # CSV出力

            # FER/DFのdominant_emoとそのscoreを出力
            # writer.writerow([i, dominant_emo_FER, emo_score, captured_emo_DF[0]['dominant_emotion'], captured_emo_DF[0]['emotion'][captured_emo_DF[0]['dominant_emotion']]])

            # FERを採用
            if captured_emo_FER and captured_emo_FER[0]['emotions']:
                writer.writerow([i, dominant_emo_FER, emo_score, 
                                 captured_emo_FER[0]['emotions']['angry'], captured_emo_FER[0]['emotions']['disgust'], captured_emo_FER[0]['emotions']['fear'],
                                 captured_emo_FER[0]['emotions']['happy'], captured_emo_FER[0]['emotions']['sad'], captured_emo_FER[0]['emotions']['surprise'],
                                 captured_emo_FER[0]['emotions']['neutral']])
            else:
                None

            print("\n ------------------------------------------------------------------------------ \n")


if __name__ == '__main__':
    name = input("イベント名を入力してください:")
    detect_emo(name)