from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'

        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}

    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"

    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 
            
        

    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'


<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()

    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
<MainScreen>:
    name: 'mainscreen'
    
    BoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        padding: '10dp'

        MDLabel:
            id: username_info
            text: 'Hello Main'
            font_style: 'H3'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]  # Adjust the height based on the content

        MDLabel:
            id: books_info
            text: ''
            font_style: 'Body1'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]  # Adjust the height based on the content

        MDRaisedButton:
            id: add_book_button
            text: 'Додати книгу'
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5}
            on_press: app.show_book_input()

        MDTextField:
            id: book_title
            pos_hint: {'center_x': 0.5}
            size_hint: (0.7, 0.1)
            hint_text: 'Введіть назву книги'
            multiline: False
            on_text_validate: app.add_book(book_title.text)
            focus: False
            opacity: 0  # Initially set opacity to 0 (invisible)


'''


class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'loginscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url  = 'https://kivy-4dd28-default-rtdb.europe-west1.firebasedatabase.app/.json'
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            to_db = {
                f'{signupEmail}':{
                    "Password": signupPassword,
                    "Username":signupUsername,
                    "Books":['test']
                }
            }
            book = []
            # signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\","Books":\"[]\"}}'})
            # signup_info = signup_info.replace(".","-")
            # signup_info = signup_info.replace("\'","")
            # to_database = json.loads(signup_info)
            # print((to_database))
            requests.patch(url = self.url,json = to_db)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = '0QjlZHsBsviGEbNRPNPdMZwq5UDBI1B0qdg9Ogvd'
    
    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        
        print(data)
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.user_books = data[supported_loginEmail].get('Books', [])
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
            # self.username_changer()
        else:
            print("user no longer exists")


    def show_book_input(self):
        book_input = self.strng.get_screen('mainscreen').ids.book_title
        add_book_button = self.strng.get_screen('mainscreen').ids.add_book_button

        if self.strng.get_screen('mainscreen').ids.add_book_button.text == 'Зберегти':
            loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
            supported_loginEmail = loginEmail.replace('.', '-')

            # Get the current user's data from Firebase
            request = requests.get(self.url + '?auth=' + self.auth)
            data = request.json()
            print(data)

            data[supported_loginEmail]['Books'].append(self.strng.get_screen('mainscreen').ids.book_title.text)
            updated_data = {supported_loginEmail: data[supported_loginEmail]}
            requests.patch(url=self.url, json=updated_data)

            # Update the books_info label on the MainScreen
            main_screen = self.strng.get_screen('mainscreen')
            main_screen.ids.books_info.text = "\n".join(data[supported_loginEmail]['Books'])
            
        if book_input.opacity == 0:  # If the text input is invisible
            book_input.opacity = 1  # Make it visible
            book_input.focus = True  # Set focus to the text input
            add_book_button.text = 'Зберегти'  # Change the button text
        else:
            book_input.opacity = 0  # Make it invisible
            add_book_button.text = 'Додати книгу'  # Change the button text
    
    def add_book(self, book_title):
        self.book = book_title

    def close_username_dialog(self,obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"welcome {self.username}"
            self.strng.get_screen('mainscreen').ids.books_info.text = "Your books:\n\n"+ "\n".join(self.user_books)

LoginApp().run()