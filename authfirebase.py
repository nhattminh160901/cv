import pyrebase
# pip install urllib3==1.26.15 requests-toolbelt==0.10.1

class FirebaseAuth():
    def firebase():
        try:
            email = "toilaminh@mail.com"
            password = "123456"

            firebaseConfig = {
            'apiKey': "AIzaSyCt60H3fUGiPv973_fMMN51lp2XXRazjF0",
            'authDomain': "arduino-firebase-vippro.firebaseapp.com",
            'databaseURL': "https://arduino-firebase-vippro-default-rtdb.firebaseio.com",
            'projectId': "arduino-firebase-vippro",
            'storageBucket': "arduino-firebase-vippro.appspot.com",
            'messagingSenderId': "437474413862",
            'appId': "1:437474413862:web:92d2b1c67528bf994fc5e7",
            'measurementId': "G-HMRKLR9EVW",
            'serviceAccount': "serviceAccountKey.json"
            }

            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            auth.sign_in_with_email_and_password(email, password)
            return firebase
        except:
            return False
        
# if FirebaseAuth.firebase():
#     st = FirebaseAuth.firebase().storage()
#     st.child("injoker.jpg").put(patch+dt_str+"_lowpass"+".png")

# if FirebaseAuth.firebase():
#                     db = FirebaseAuth.firebase().database()
#                     db.child("new_life").update({"repeat_times":int(self.entryRT.get())})
#                     db.child("new_life").update({"min_v_"+str(i+1):"processing", "min_a_"+str(i+1):"processing"}) #min
#                     db.child("new_life").update({"max_v_"+str(i+1):"processing", "max_a_"+str(i+1):"processing"}) #max
#                     db.child("new_life").update({"min_v_"+str(i+1):listValues[i][0][listValues[i][2].tolist().index(min(listValues[i][2]))],
#                                                 "min_a_"+str(i+1):min(listValues[i][2])}) #min
#                     db.child("new_life").update({"max_v_"+str(i+1):listValues[i][0][listValues[i][2].tolist().index(max(listValues[i][2]))],
#                                                 "max_a_"+str(i+1):max(listValues[i][2])}) #max