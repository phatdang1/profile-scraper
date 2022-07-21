from deepface import DeepFace
import cv2

# fuction use to predict gender
def predict(path):
    img = cv2.imread(path)
    gender = DeepFace.analyze(img, actions = ['gender'], enforce_detection=False)
    print(gender['gender'])
    if gender['gender'] == 'Woman':
        return 'female'
    else:
        return 'male'