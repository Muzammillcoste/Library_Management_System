from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from oracle_test import view_all_book, delete_book, search_books

book_list = list(view_all_book())
labelStartTags = ['Book ID: ', 'Name: ', "Author: ", "Publisher: ", 'Number of copies: ', 'Shelf Location: ']

class RemoveBookPopup(Popup):

    def __init__(self, **kwargs):
        super(RemoveBookPopup, self).__init__(**kwargs)
        self.title = "Remove Book"
        self.size_hint = (None, None)
        self.size = ("300dp", "200dp")
        self.layout = BoxLayout(orientation='vertical', spacing=20)

        self.textInp = TextInput(hint_text = "Enter Book ID", size_hint = (1, None), size = ("300dp", "50dp"), multiline = False)
        self.layout.add_widget(self.textInp)

        btnLayout = BoxLayout(spacing = 10)
        enter = Button(text = "Enter", size_hint = (1,None), size = ("100dp", "40dp"), color = "blue",
                       on_release = self.enterBtnFunc)
        btnLayout.add_widget(enter)

        goBack = Button(text="Go Back", size_hint=(1, None), size=("100dp", "40dp"), color="red",
                       on_release=self.dismiss)
        btnLayout.add_widget(goBack)
        self.layout.add_widget(btnLayout)
        self.content = self.layout

    def enterBtnFunc(self, instance):
        bId = self.textInp.text
        if bId.isdigit():
            bId = int(self.textInp.text)
        bInfo = search_books(bId)

        if bInfo:
            self.layout.clear_widgets()
            for i in range(6):
                labl = Label(text= f"{labelStartTags[i]}: {bInfo[i]}")
                self.layout.add_widget(labl)

            bLayout = BoxLayout()
            remove = Button(text = "Remove", color = "red", on_release= lambda instance: self.removeConfirmation(instance,bId))
            cancel = Button(text = "Cancel", color = "blue", on_release = self.dismiss)
            bLayout.add_widget(remove)
            bLayout.add_widget(cancel)
            self.layout.add_widget(bLayout)
            self.size = ("300dp", "400dp")

        else:
            self.layout.clear_widgets()
            labl = Label(text="Book Id Not Found")
            self.layout.add_widget(labl)
            close = Button(text="close", color = 'red', on_release = self.dismiss)
            self.layout.add_widget(close)

    def removeConfirmation(self, instance, removingId):
        status = delete_book(removingId)
        self.layout.clear_widgets()
        labl = Label(text= status)
        self.layout.add_widget(labl)
        goBack = Button(text= "Go Back", background_color = "blue", on_release = self.dismiss)
        self.layout.add_widget(goBack)
        self.size = ('350dp','200dp')

