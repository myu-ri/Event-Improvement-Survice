from .component_make_picture import *
from .component_detect_people import *
from .component_detect_emotion import * 
from .component_aggregate import *
from .component_emo_mean import *
import shutil


class Main:
    def __init__(self, input_data):
        # self.name = input("イベント名を入力してください:")
        self.name = input_data

        try:
            #predict・フォルダの削除
            shutil.rmtree('./eisapp/event_Improvement_survice/detect_face_emotion/runs/detect/predict')
        except:
            None

    def act(self):
        # カメラ起動・データ作成
        save_frame_camera_cycle(0, './eisapp/event_Improvement_survice/detect_face_emotion/data/' + self.name, 'camera_capture_cycle', 30)

        # YOLOによる物体検知
        detect_people(self.name)

        # FERによる表情分析
        detect_emo(self.name)

        # 感情分析結果集計
        aggregate(self.name)

        # 感情推移平均
        emo_mean(self.name)

if __name__ == '__main__':
    main = Main()
    main.act()