from deepface import DeepFace
import cv2

def predict(path):
    img = cv2.imread(path)
    gender = DeepFace.analyze(img, actions = ['gender'], enforce_detection=False)
    if gender == 'Women':
        return 'female'
    else:
        return 'male'