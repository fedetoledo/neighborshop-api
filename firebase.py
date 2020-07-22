		
import pyrebase
from getpass import getpass

firebaseConfig = {
  #Key must be wrapped in " "
    "apiKey": "AIzaSyD7b5sNyKgzDX6NMCwXaor7rR3_pf9MBJ0",
    "authDomain": "barrio-ecommerce.firebaseapp.com",
    "databaseURL": "https://barrio-ecommerce.firebaseio.com",
    "projectId": "barrio-ecommerce",
    "storageBucket": "barrio-ecommerce.appspot.com",
    "messagingSenderId": "110705840395",
    "appId": "1:110705840395:web:a10a96cc64690d18ee520e"
}


firebase = pyrebase.initialize_app(firebaseConfig)


# auth = firebase.auth()



# #create users
# user = auth.create_user_with_email_and_password(email, password)
# print("Success .... ")


# login = auth.sign_in_with_email_and_password(email, password)

# #send email verification
# auth.send_email_verification(login['idToken'])


# #reset the password
# auth.send_password_reset_email(email)

# print("Success ... ")