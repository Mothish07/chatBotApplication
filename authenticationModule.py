import pyrebase

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
auth = firebase.auth()

def signUp(email,password,name):
   try:
      if len(password) < 8:
         return {"success":False ,"error":"Password is weak... Please Give more than 8 characters"}
      else:
         new_user = auth.create_user_with_email_and_password(email,password)
         auth.update_user(new_user["idToken"], {"display_name": name})
         #auth.send_email_verification(new_user["idToken"])
         return {"success":True ,"user":{"name": name}}   
   except Exception as e:
      error_message = str(e)
      if "INVALID_EMAIL" in error_message:
         return {"success": False, "error": "Invalid email format. Please enter a valid email address."}
      elif "EMAIL_EXISTS" in error_message:
            return {"success": False, "error": "Email already registered. Please use a different email address."}
      else:
         return {"success": False, "error":f"Something Went Wrong Please Try again!!{error_message}"}
  


def signIn(email,password):
   try:
      user = auth.sign_in_with_email_and_password(email,password)
      return {"success":True ,"user":user}
   except auth.AuthError as auth_error:
        if "INVALID_PASSWORD" in str(auth_error):
            return {"success": False, "error": "Invalid password.."}
        elif "USER_NOT_FOUND" in str(auth_error):
            return {"success": False, "error": "Invalid email.."}
        else:
            return {"success": False, "error":"Something Error in Login Credintials..."}
   except Exception:
      return {"success":False,"error":"Something Went Wrong Please Try again!!!"}
   
def signOut():
   try:
      auth.signOut()
      return {"success":True}
   except auth.AuthError:
        return {"success": False, "error":"You are Logged In.."}
   except Exception:
      return {"success":False,"error":"Something Went Wrong Please Try again!!!"}
   
def reset_password(email):
    try:
        auth.send_password_reset_email(email)
        return {"success": True}
    except auth.AuthError as auth_error:
        error_message = str(auth_error)
        if "EMAIL_NOT_FOUND" in error_message:
            return {"success": False, "error": "No User Found in this email. Please Check Email or Create New Account"}
        else:
            return {"success": False, "error": "Domething error in Credintials Please Try again!!"}
    except Exception:
      return {"success":False,"error":"Something Went Wrong Please Try again!!!"}


