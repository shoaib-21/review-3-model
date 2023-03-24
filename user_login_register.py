import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
from datetime import date

def initializeDB(path):
        if not firebase_admin._apps:
            cred = credentials.Certificate(path)
            app = firebase_admin.initialize_app(cred)
            db = firestore.client()
            return db
def create_entry(name,image_url,db):
    #db = initializeDB(r'/home/pi/facial-recognition-main/user-login-register-firebase.json')
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", t)
    current_date = today.strftime("%d-%b-%Y")
    data={
        u'name':name,
        u'login time':current_time,
        u'date':current_date,
        u'image':image_url
    }
    db.collection(u'user-login-details').document().set(data)

# def read_db(db):
#     docs = db.collection('user-login-details').document().stream()
#     # print({docs.to_dict()})
#     for doc in docs:
#         if doc.exists:
#             print(f'Document data: {doc.to_dict()}')
#         else:
#             print(u'No such document!')

# path = r'C:\Users\mohd noor ahmed\OneDrive\Desktop\Coding\python\user-login-register-firebase.json'
# db = initializeDB(path)
# create_entry(db,u'mna',u'03:28:12 PM',u'19-Mar-2023',u'helloiamnoor.com')
