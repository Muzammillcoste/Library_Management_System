from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from oracle_test import insert_book, view_all_book

book_list = list(view_all_book())

class AddBookPopup(Popup):
    # Create the layout for the popup

    book_id = book_list[-1][0] + 1
    book_title = None
    author_name = None
    publisher_name = None
    num_copies = None
    shelf_location = None

    textHint = [f'Book Id: {book_id}', 'Enter Book Name', 'Enter Author Name', 'Enter Publisher Name',
                'Enter Number of Copies', 'Enter shelf location']
    txtInpIDs = ['id', 'name', 'aname', 'pname', 'noc', 'shelf']

    def __init__(self, **kwargs):
        super(AddBookPopup, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Create the input text fields
        for i in range(6):
            text_input = TextInput(hint_text= self.textHint[i])
            setattr(text_input,'id',self.txtInpIDs[i])
            self.layout.add_widget(text_input)
            if i == 0:
                text_input.disabled = True

        bLayout = BoxLayout()
        # Create the buttons
        btn1 = Button(text='Add', background_color = 'blue', on_release = self.addBook)
        btn2 = Button(text='cancel', background_color = 'red', on_release = self.dismiss)
        bLayout.add_widget(btn1)
        bLayout.add_widget(btn2)
        self.layout.add_widget(bLayout)
        # Add the layout to the popup
        self.content = self.layout

    def addBook(self, instance):
        # Get the text from each TextInput field
        for widget in self.layout.children:
            if isinstance(widget, TextInput):
                if widget.id == 'id':
                    self.book_id = self.book_id
                elif widget.id == 'name':
                    self.book_title = widget.text
                elif widget.id == 'aname':
                    self.author_name = widget.text
                elif widget.id == 'pname':
                    self.publisher_name = widget.text
                elif widget.id == 'noc':
                    self.num_copies = widget.text
                elif widget.id == 'shelf':
                    self.shelf_location = widget.text

        txt = ''
        if self.book_title == "" or self.book_title == None:
            txt = "Book title missing !!!"
        elif self.num_copies == "" or self.num_copies == None or (not self.num_copies.isdigit()):
            txt = "Number of copies must be a number !!!"
        else:
            self.num_copies = int(self.num_copies)
            txt = insert_book(book_id=self.book_id, book_title=self.book_title, author_name=self.author_name, publisher=self.publisher_name,
                        number_of_copies=self.num_copies, shelf_location=self.shelf_location)

        self.layout.clear_widgets()
        self.layout.add_widget(Label(text = txt))
        self.layout.add_widget(Button(text = "close", color = 'red', size_hint = (None, None) , size = ('100dp', '50dp'),
                                      pos_hint = {'x': .3} ,on_release = self.dismiss))
        self.size = ('350dp', '200dp')




