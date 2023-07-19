from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)

        # Create the root layout
        self.root = BoxLayout(orientation='vertical', padding = 10)

        # Create the background watermark image
        watermark = Image(source='iconLib.png',allow_stretch=True, keep_ratio=False, opacity=0.3)  # Replace 'watermark.png' with your watermark image

        # Add the watermark to the root layout
        self.add_widget(watermark)

        # Create the main heading label
        self.heading_label = Label(text='[b][u]The Online Library[/u][/b]', font_size='40sp', size_hint=(1, 0.2), markup= True)

        # Add the heading label to the root layout
        self.root.add_widget(self.heading_label)

        # Create the description label
        self.description_label = Label(text='''
This online library is created as the complex engineering problem for the database management systems course.
It has been made by collaboration of four computer system engineering students of batch 2021.
This library provides you the facility to login the application if you got the admin id and password.
After you have successfully login, you may add new books in the book records or issue or remove any book.
You may also view members or add or update or remove the library registered members.
If a book is issued to a member, the record is kept about issue date, due date and return date is also recorded when book is returned.
For more information about usage of application please refer to the help section.''',
                      font_size='20sp',
                      size_hint=(1, 0.6),
                      size=(Window.width * 0.8, Window.height * 0.2),
                      text_size=(Window.width * 0.8, None),
                      halign='left',
                      valign='middle',
                      color='black',
                      markup=True)
        self.description_label.bind(texture_size=self.description_label.setter('size'))

        # Add the description label to the root layout
        self.root.add_widget(self.description_label)

        # Create the return button
        self.return_button = Button(text='Return', size_hint=(None,None), size = ('200dp', '50dp'), pos_hint = {'x': 0.35},
                                    background_color="lightgray", color = "cyan")

        # Add the return button to the root layout
        self.root.add_widget(self.return_button)

        # Set the root layout as the screen's root widget
        self.add_widget(self.root)


