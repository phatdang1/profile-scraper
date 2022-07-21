from deepface import DeepFace
import cv2

def predict(path):
    img = cv2.imread(path)
    gender = DeepFace.analyze(img, actions = ['gender'], enforce_detection=False)
    print(gender['gender'])
    if gender['gender'] == 'Woman':
        return 'female'
    else:
        return 'male'
n = predict('images/0.jpg')
print(n)