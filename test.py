from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from authenticationModule import signUp, signIn, signOut, reset_password

class AuthApp(App):
    def build(self):
        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        self.name_input = TextInput(hint_text='Name', multiline=False)

        self.signup_button = Button(text='Sign Up', on_press=self.signup)
        self.signin_button = Button(text='Sign In', on_press=self.signin)
        self.signout_button = Button(text='Sign Out', on_press=self.signout)
        self.reset_password_button = Button(text='Reset Password', on_press=self.reset_password)

        self.result_label = Label(text='', halign='center')

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.name_input)
        layout.add_widget(self.signup_button)
        layout.add_widget(self.signin_button)
        layout.add_widget(self.signout_button)
        layout.add_widget(self.reset_password_button)
        layout.add_widget(self.result_label)

        return layout

    def signup(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        name = self.name_input.text

        response = signUp(email, password, name)

        if response["success"]:
            self.result_label.text = response["response_msg"]
        else:
            self.result_label.text = response["response_msg"]

    def signin(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        response = signIn(email, password)

        if response["success"]:
            self.result_label.text = f"Welcome, {response['user']}!"
        else:
            self.result_label.text = response["response_msg"]

    def signout(self, instance):
        response = signOut()

        if response["success"]:
            self.result_label.text = response["response_msg"]
        else:
            self.result_label.text = response["response_msg"]

    def reset_password(self, instance):
        email = self.email_input.text

        response = reset_password(email)

        if response["success"]:
            self.result_label.text = "Password reset email sent."
        else:
            self.result_label.text = response["response_msg"]

if __name__ == '__main__':
    AuthApp().run()
