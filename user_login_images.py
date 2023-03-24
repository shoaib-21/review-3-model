import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import time


def get_config():
    config = {
    'apiKey': "AIzaSyANNCO3ZUw2pxPofilWZR8USGFSu1qkkGE",
    'authDomain': "user-login-images-d7c8f.firebaseapp.com",
    'projectId': "user-login-images-d7c8f",
    'storageBucket': "user-login-images-d7c8f.appspot.com",
    'messagingSenderId': "833114978320",
    'appId': "1:833114978320:web:b0be8255c9399929103295",
    'measurementId': "G-0H30VSG50D",
    'databaseURL':'gs://user-login-images-d7c8f.appspot.com'
    }
    return config

def initializeImagedb():
        config = get_config()
        path=r'/home/pi/facial-recognition-main/user_login_images.json'
        cred = credentials.Certificate(path)
        return cred
        #firebase_admin.initialize_app(cred,config)
        #client = storage.client.Client()

        
def uploadImage(cred,folder,cloudFilename,imgbuf):
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred,{'storageBucket':"user-login-images-d7c8f.appspot.com"})
        #mgbuf= cv2.imencode('.png',frame)[1].tobytes()
        bucket = storage.bucket("user-login-images-d7c8f.appspot.com")
        blob = bucket.blob(folder+'/'+cloudFilename+'.png')
        blob.upload_from_string(imgbuf,content_type='image/png')
        blob.make_public()
        # time.sleep(0.5)
        url = blob._get_download_url(None)
        print(url)
        return url



       
    