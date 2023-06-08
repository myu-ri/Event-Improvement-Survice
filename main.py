from component_make_picture import *
from component_detect_people import *
from component_detect_emotion import * 
from component_aggregate import *
from component_emo_mean import *
import shutil

try:
    #predict・フォルダの削除
    shutil.rmtree('runs/detect/predict')
except:
    None

# カメラ起動・データ作成
name = input("イベント名を入力してください:")
save_frame_camera_cycle(0, 'data/' + name, 'camera_capture_cycle', 30)

# YOLOによる物体検知
detect_people(name)

# FERによる表情分析
detect_emo(name)

# 感情分析結果集計
aggregate(name)

# 感情推移平均
emo_mean(name)