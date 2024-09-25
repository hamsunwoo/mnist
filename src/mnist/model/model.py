import numpy as np
from PIL import Image
from keras.models import load_model
import os

def get_model():
    # 모델 로드
    f= __file__
    dir_name = os.path.dirname(f)
    model_path = os.getenv('MODEL_PATH', os.path.join(dir_name, "mnist240924.keras"))
    model = load_model(f'{model_path}')
    
    return model

def get_model_name():
    f= __file__
    dir_name = os.path.dirname(f)
    model_path = os.getenv('MODEL_PATH', os.path.join(dir_name, "mnist240924.keras"))

    return model_path

# 사용자 이미지 불러오기 및 전처리
def preprocess_image(file_path):
    img = Image.open(file_path).convert('L')  # 흑백 이미지로 변환
    img = img.resize((28, 28))  # 크기 조정

    # 흑백 반전
    img = 255 - np.array(img)  # 흑백 반전
    #img = np.array(img)

    img = img.reshape(1, 28, 28, 1)  # 모델 입력 형태에 맞게 변형
    img = img / 255.0  # 정규화

    return img

# 예측
def predict_digit(file_path):
    model = get_model()
    img = preprocess_image(file_path)
    prediction = model.predict(img)
    digit = np.argmax(prediction)

    return digit

