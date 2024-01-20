import pyrebase
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("/home/mothish/Projects/miniproject/chatbotx-338c8-firebase-adminsdk-rpsht-a5226dd47b.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
   "apiKey": "AIzaSyCOLYfF47_xfkTEZy8X3A4hwUFaCyLCals",
   "authDomain": "chatbotx-338c8.firebaseapp.com",
   "projectId": "chatbotx-338c8",
   "storageBucket": "chatbotx-338c8.appspot.com",
   "messagingSenderId": "346958153567",
   "databaseURL":"https://trialauth-7eea1.firebaseio.com",
   "appId": "1:346958153567:web:a52241681709cf73e8d8ea",
   "measurementId": "G-YKGQFC8GNV"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth_pyrebase = firebase.auth()

def signUp(email,password,name):
   try:
      if len(password) < 8:
         return {"success":False ,"error":"Password is weak... Please Give more than 8 characters"}
      else:
         new_user = auth_pyrebase.create_user_with_email_and_password(email,password)
         uid = new_user["localId"]
         user = auth.update_user(uid,display_name=name)
         auth_pyrebase.send_email_verification(new_user["idToken"])
         return {"success":True ,"user":name,"response_msg":"Successfully Signed Up"}   
   except Exception as e:
      error_message = str(e)
      if "INVALID_EMAIL" in error_message:
         return {"success": False, "response_msg": "Invalid email format. Please enter a valid email address."}
      elif "EMAIL_EXISTS" in error_message:
            return {"success": False, "response_msg": "Email already registered. Please use a different email address."}
      else:
         return {"success": False, "response_msg":f"Something Went Wrong Please Try again!!{e}"}
  


def signIn(email,password):
   try:
      user = auth_pyrebase.sign_in_with_email_and_password(email,password)

      return {"success":True ,"user":user["displayName"],"response_msg":"Sucessfully Signed In"}
   except Exception as e:
        if "INVALID_LOGIN_CREDENTIALS" in str(e):
            return {"success": False, "response_msg": "Invalid login credentials.."}
        elif "INVALID_EMAIL" in str(e):
           return {"success": False, "response_msg": "Invalid Email ID.."}
        else:
           return {"success":False,"response_msg":"Something Went Wrong Please Try again!!!"}
   
      
   
def signOut():
   try:
      auth_pyrebase.current_user = None
      return {"success": True, "response_msg": "Successfully signed out."}

   except Exception:
      return {"success":False,"response_msg":"Something Went Wrong Please Try again!!!"}
   
def reset_password(email):
    try:
        auth_pyrebase.send_password_reset_email(email)
        return {"success": True}
    except Exception as e:
        if "EMAIL_NOT_FOUND" in str(e):
            return {"success": False, "response_msg": "No User Found in this email. Please Check Email or Create New Account"}
        elif "INVALID_EMAIL" in str(e):
           return {"success": False, "response_msg": "Invalid Email ID.."}
        else:
            return {"success":False,"response_msg":"Something Went Wrong Please Try again!!!"}

      


