from authenticationModule import signUp,signOut,signIn


response = signUp("tetedssl@gmail.com","12346789","Example")

if response["success"]:
            print("Sign Up Successful. User:", response["user"])
else:
            print("Sign Up Failed. Error:", response["error"])