from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super(HelpScreen, self).__init__(**kwargs)

        # Create the main layout
        self.layout = BoxLayout(orientation="vertical", padding=10)

        # Create the background watermark image
        watermark = Image(source='iconLib.png', allow_stretch=True, keep_ratio=False, opacity=0.3)  # Replace 'watermark.png' with your watermark image

        # Add the watermark to the layout
        self.add_widget(watermark)

        # Create the main heading label
        self.heading_label = Label(text='[b][u]The Help Section[/u][/b]', font_size='40sp', size_hint=(1, 0.2), color = 'black', markup=True)

        # Add the heading label to the content layout
        self.layout.add_widget(self.heading_label)

        self.start_text = Label(
            text='This section contain breif description of the three button present on previous screen, which are as follows:',
            font_size='20sp',
            size_hint=(1, None),
            text_size=(Window.width * 0.8, None),
            color='black',
            markup=True)
        self.layout.add_widget(self.start_text)

        self.homeLabel = Label(
            text=f'[ref=link][u]1. Home[/u][/ref]',
            font_size='20sp',
            size_hint=(1, None),
            text_size=(Window.width * 0.8, None),
            color='black',
            markup=True,
            on_ref_press = lambda x,y: self.labelPressed(labelName='home')
        )
        self.layout.add_widget(self.homeLabel)

        self.bookLabel = Label(
            text=f'[ref=link][u]2. Books[/u][/ref]',
            font_size='20sp',
            size_hint=(1, None),
            text_size=(Window.width * 0.8, None),
            color='black',
            markup=True,
            on_ref_press=lambda x,y: self.labelPressed(labelName='books')
        )
        self.layout.add_widget(self.bookLabel)

        self.memberLabel = Label(
            text=f'[ref=link][u]3. Members[/u][/ref]',
            font_size='20sp',
            size_hint=(1, None),
            text_size=(Window.width * 0.8, None),
            color='black',
            markup=True,
            on_ref_press=lambda x,y: self.labelPressed(labelName='members')
        )
        self.layout.add_widget(self.memberLabel)

        self.endText = Label(
            text='Click on any above defined labels to get more information',
            font_size='20sp',
            size_hint=(1, None),
            text_size=(Window.width * 0.8, None),
            color='black',
            markup=True
        )
        self.layout.add_widget(self.endText)

        # Create the return button
        self.return_button = Button(text='Return', size_hint=(None, None), size=('200dp', '50dp'), pos_hint={'x': 0.35},
                               background_color="lightgray", color="cyan")

        # Add the return button to the content layout
        self.layout.add_widget(self.return_button)

        # Set the main layout as the screen's root widget
        self.add_widget(self.layout)

    def labelPressed(self, labelName):
        self.layout.clear_widgets()
        txt = ''
        if labelName == 'home':
            txt = '''
Home:
The Home button opens a menu which contains four items:
1. About Us: Here you can get few details about this project.
2. Add Admin: Through this you may create a new admin account. The steps are simple and easy.
3. Staff Details: This option has some important details:
        Once you press this menu item a popup will open with a search bar, a button with text "add staff" and a close button.
        If you search a staff member by name or id you will get another popup with the staff attributes and update and delete button.
        The process is easy to follow and relevant messages are provided.
        On pressing add staff button the necessary staff attributes are taken an input and stored in the database.
3. Logout: Self-explanatory.'''

        elif labelName == 'books':
            txt ='''
Books:
The Books Button will open a menu for you with four different items:
1. Show Books: This shall take you to a new screen which contains all books in our book bank.
   The screen contains three columns each column has multiple rows with book id and name.
   Each of this entry is a hyperlink, on click you will find a popup menu which contains book information.
   On below the popup, there are three buttons:	
   i.   Remove: You may remove/delete the book.
   ii.  Issue: Provide book to member
   iii. close: Close the popup.   
   Each of these operations are simple and easy. No further description is required.
  
2. AddBook: Add a new book to the bank.
3. Issue Book: Issue book to member. A slight different implementation from the method defined in book bank.
4. Remove Book: Remove Book from book bank. Simple and easy operations, handy to follow.'''

        elif labelName == 'members':
            txt = '''
Members:
This Buttons opens a screen with a search bar and five operations on left of screen:
1. Add Member: Register a member in record.
2. Remove Member: Remove a member from record.
3. Update Member: Update a member current information. Except ID and name.
4. Return Book: Keep record of book when it is returned.
5. Go Back: Return to previous Screen

While the rest of screen has a single cloumn and multiple rows each, each column entry is a member id and name which is hyperlink and on click open a popup which contains member information.'''

        description_label = Label(
            text=txt,
            font_size='20sp',
            size_hint=(1, 1),
            size=(Window.width * 0.8, Window.height * 0.2),
            text_size=(Window.width * 0.8, None),
            halign='left',
            valign='top',
            color='black',
            markup=True)

        self.go_back = Button(text='Go Back', size_hint=(None, None), size=('200dp', '50dp'), pos_hint={'x': 0.35},
                              background_color="lightgray", color="cyan", on_release = self.changeLayout)

        self.layout.add_widget(description_label)
        self.layout.add_widget(self.go_back)

    def changeLayout(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.heading_label)
        self.layout.add_widget(self.start_text)
        self.layout.add_widget(self.homeLabel)
        self.layout.add_widget(self.bookLabel)
        self.layout.add_widget(self.memberLabel)
        self.layout.add_widget(self.endText)
        self.layout.add_widget(self.return_button)
