import faceRecog
import RRead
import time
import lock
import userdb
import find_fingerprint
import user_login_images
import user_login_register
import lcd_display as lcd


path = '/home/pi/facial-recognition-main/adminsdk.json'
db = userdb.initializeDB(path)
db2 = user_login_register.initializeDB(r'/home/pi/facial-recognition-main/user-login-register-firebase.json')
print('db2 :' , db2)
cred = user_login_images.initializeImagedb()

while True:
#    lock.doorlock()
    authorizeduser =''
    rfid,rfid_username = RRead.readRfid()
    
#     if rfid_username == "none":
#         pass
    lcd.display_msg('USE RFID TAG OR ','    BIOMETRIC   ')
    if rfid_username != 'none' :
        print(rfid_username)
        user_auth = userdb.get_rfid(db,rfid)
        #lcd.display_msg('please look in ','   the camera')
        if user_auth == rfid_username:
            print('please look in the camera')
            lcd.display_msg('PLEASE LOOK IN  ','   THE CAMERA')
            time.sleep(1.5)
            authorizeduser = faceRecog.Face(user_auth)
        else:
            lcd.display_msg('  INVALID RFID  ','   ACCESS DENIED!!  ')
            time.sleep(2)
            #print(authorizeduser)
            
    else:    
        empid= find_fingerprint.get_fingerprint()

        if empid == None:
            lcd.display_msg('USER NOT FOUND ','   ACCESS DENIED!!  ')
            time.sleep(2)
            continue
        elif empid == 'none':
            continue
        else :
            #print(empid)
            username=userdb.get_empname(db,empid)
            print(username)
            lcd.display_msg('PLEASE LOOK IN  ','   THE CAMERA')
            time.sleep(1.5)
            authorizeduser = faceRecog.Face(username)
            
    if authorizeduser == False:
            print("Face not match!! Access denied")
            lcd.display_msg('FACE NOT MATCHED ','  ACCESS DENIED!')
            time.sleep(2)
    elif authorizeduser == '':
        print('')
    else:    
        print('Access granted')
        print("string ",authorizeduser)
        lcd.display_msg('FACE MATCHED ',' ACCESS GRANTED! ')
        #imgUrl=user_login_images.uploadImage(cred,username,username,authorizeduser)
        #user_login_register.create_entry(username,imgUrl,db2)
        #print("door unlocks...")
        
        lock.doorunlock()
        
            
''' print("1. RFID /t 2.FINGERPRINT /n" )
    choice = int(input("enter a choice: "))
    authorizeduser=""
    if(choice == 1):
        rfid,rfid_username = RRead.readRfid()
        print(rfid_username)
        #print(rfid)
        c
        else:
            print("unauthorized rfid card... please try again")
            continue
    elif(choice == 2):
        empid = find_fingerprint.get_fingerprint()
        print(empid)
        if empid == False:
            print("fingerperint not found....  please try again")
            continue
        username=userdb.get_empname(db,empid)
        print(username)
        	
#         if template == 1:
#             username = "shaik sharfuddin"
#         elif template == 2:
#             username = "mustafa"
#         elif template == 3:
#            username = "noor"
        authorizeduser = faceRecog.Face(username)
        print(authorizeduser)
        
    if authorizeduser == False:
        print("Face not matched!!!!   door cannot be open")
        
    else:
        #imgUrl=user_login_images.uploadImage(cred,username,username,authorizeduser)
        #user_login_register.create_entry(username,imgUrl,db2)
        #print("door unlocks...")
        lock.doorunlock()
'''
