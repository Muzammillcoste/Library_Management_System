from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch,OneLineAvatarIconListItem
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import date, timedelta
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivymd.uix.snackbar import Snackbar
from del10 import AddBookPopup
from del12 import RemoveBookPopup
from del13 import MemberScreen
from about import AboutScreen
from Help import HelpScreen
from oracle_test import search_books, view_all_book, login, add_admin, generateAdminID,\
    update_book, borrow_book, search_member, search_staff, update_staff, delete_staff,\
    generateStaffID, insert_staff

labelStartTags = ['Book ID: ', 'Name: ', "Author: ", "Publisher: ", 'Number of copies: ', 'Shelf Location: ']

# Create a screen manager
sm = ScreenManager()

Builder.load_string(
    """
<LoginScreen>:
    FloatLayout:
        orientation: 'vertical'
        Image:
            source: 'library_1.jpg'  # Background image
            allow_stretch: True
            keep_ratio: False
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.4
            height: self.minimum_height
            pos_hint: {"center_y": 0.5}
        
            BoxLayout:
                spacing: 15
                orientation: 'vertical'
                size_hint: 0.5, 0.5
                height: self.minimum_height
                pos_hint: {"center_x": 0.5}
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20, 20, 20, 20]
        
                MDLabel:
                    id: top
                    text: "Login"
                    theme_text_color: "Secondary"
                    font_style: "H5"
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
        
                MDTextField:
                    id: adminId
                    hint_text: "Admin ID"
                    size_hint_y: None
                    height: "48dp"
                    pos_hint: {"center_x": 0.5}
                    mode: "rectangle"
        
                MDTextField:
                    id: pwd
                    hint_text: "Password"
                    size_hint_y: None
                    height: "48dp"
                    pos_hint: {"center_x": 0.5}
                    mode: "rectangle"
                    password: True
        
                MDFlatButton:
                    text: "Sign In"
                    size_hint: 0.5, None
                    md_bg_color: 'cyan'
                    height: "48dp"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.root.current_screen.loginAdmin()
                    # app.root.current = "portal"
    
<AddAdmin>:
    FloatLayout:
        orientation: 'vertical'
        Image:
            source: 'lib_signup.jpg'  # Background image
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.6
            height: self.minimum_height
            pos_hint: {"center_y": 0.5}
        
            BoxLayout:
                spacing: 5
                orientation: 'vertical'
                size_hint: 0.5, 0.6
                height: self.minimum_height
                pos_hint: {"center_x": 0.5}
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [20, 20, 20, 20]
        
                MDLabel:
                    text: "Add Account"
                    theme_text_color: "Secondary"
                    font_style: "H4"
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
                     
                MDTextField:
                    id: adminID
                    hint_text: "Admin ID"
                    disabled: True
                    size_hint_y: None
                    height: "36dp"
                    pos_hint: {"center_x": 0.5}
                    mode: "rectangle"
        
                MDTextField:
                    id: staffID
                    hint_text: "Staff ID"
                    size_hint_y: None
                    height: "36dp"
                    pos_hint: {"center_x": 0.5}
                    mode: "rectangle"
        
                MDTextField:
                    id: pwd
                    hint_text: "Password"
                    size_hint_y: None
                    height: "36dp"
                    pos_hint: {"center_x": 0.5}
                    mode: "rectangle"
                    password: True
        
                MDFlatButton:
                    text: "ADD"
                    size_hint: 0.5, None
                    md_bg_color: 'gray'
                    height: "48dp"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.root.current_screen.addBtn()
                    #app.root.current = "portal"  
        
                MDFlatButton:
                    text: "Cancel"
                    size_hint: 0.5, None
                    md_bg_color: 'red'
                    height: "48dp"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.root.current = "portal"  
    
<RightContentCls>
    disabled: True
    adaptive_size: True
    pos_hint: {"center_y": .5}
    
    MDIconButton:
        icon: root.icon
        user_font_size: "16sp"
        md_bg_color_disabled: 0, 0, 0, 0
    
    MDLabel:
        text: root.text
        font_style: "Caption"
        adaptive_size: True
        pos_hint: {"center_y": .5}
    
<Item>
    
    IconLeftWidget:
        icon: root.left_icon
    
    RightContentCls:
        id: container
        icon: root.right_icon
        text: root.right_text    
    
<PopupContent>:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '10dp'
    
    Label:
        id: 1
        text: 'ID: '
    Label:
        id: 2
        text: 'Name: '
    Label:
        id: 3
        text: 'Author: '
    Label:
        id: 4
        text: 'Publisher: '
    Label:
        id: 5
        text: 'Number of Copies: '
    Label:
        id: 6
        text: 'Shelf Location: '
    
    BoxLayout:
        spacing: '10dp'
        size_hint: 1, None
        height: '48dp'
    
        Button:
            id: B1
            text: 'Update'
            # on_release:
            #     # app.root.current_screen.close_popup() 
            #     # app.root.current_screen.show_deletion_popup()
            #     app.update_book()
        Button:
            id: B2
            text: 'Issue Book'
            on_release:
                app.root.current_screen.close_popup()
                app.root.current_screen.show_issue_popup(root.ids['1'].text)
        Button:
            id: B3
            text: 'close'
            background_color: 'red'
            on_release: 
                app.root.current_screen.close_popup()             
    """
    )

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        layout = BoxLayout()
        image = Image(source='lib.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(image)

        self.add_widget(layout)

    def on_enter(self, *args):
        # Display welcome screen for 3 seconds
        Clock.schedule_once(self.switch_to_login, 3)

    def switch_to_login(self, *args):
        self.manager.current = 'login'


class LoginScreen(MDScreen):

    def loginAdmin(self):
        adminID = self.ids['adminId'].text
        if adminID.isdigit() :
            adminID = int(adminID)
        pwd = self.ids['pwd'].text
        if login(admin_id=adminID, password=pwd):
            self.ids['top'].text = "Login"
            self.ids['top'].color = 'gray'
            self.ids['adminId'].text = ""
            self.ids['pwd'].text = ""
            MyApp.goto('portal')
        else:
            self.ids['top'].text = "Invalid id or password"
            self.ids['top'].color = 'red'


class AddAdmin(MDScreen):
    newID = generateAdminID()
    def __init__(self, **kwargs):
        super(AddAdmin, self).__init__(**kwargs)
        self.ids['adminID'].hint_text = str(self.newID)

    def addBtn(self):
        staffid  = self.ids['staffID'].text
        pwd = self.ids['pwd'].text
        status = add_admin(staff_id=staffid, password=pwd)
        if status == "Admin added successfully.":
            Snackbar(text=(" "*30)+"Admin added successfully.").open()
            MyApp.goto('portal')
        else:
            Snackbar(text=(" "*80)+status).open()

class RightContentCls(IRightBodyTouch, MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()


class Item(OneLineAvatarIconListItem):
    left_icon = StringProperty()
    right_icon = StringProperty()
    right_text = StringProperty()

class Portal(Screen):
    def __init__(self, **kwargs):
        super(Portal, self).__init__(**kwargs)
        layout = FloatLayout()
        # Set the background image
        background_image = Image(source="lib_portal.jpg", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        layout.add_widget(MDRoundFlatButton(text="Home", pos_hint={'x': 0.01, 'top': 0.98},on_release = self.open_menu_for_home))
        layout.add_widget(MDRoundFlatButton(text="Books", pos_hint={'x': 0.12, 'top': 0.98}, on_release = self.open_menu_for_books))
        layout.add_widget(MDRoundFlatButton(text="Members", pos_hint={'x': 0.24, 'top': 0.98},
                                            on_release = lambda x: MyApp.goto(MyApp, name="member")))
        layout.add_widget(MDRoundFlatButton(text="Help", pos_hint={'x': 0.38, 'top': 0.98},
                                            on_release = lambda x: MyApp.goto(MyApp, name="help")))

        self.add_widget(layout)

    def open_menu_for_home(self, instance):
        # Create a dropdown menu
        menu_items = [
            {"viewclass": "Item", "text": "About Us", "left_icon": "iconLib.png", "height": dp(56),
                                                "on_release": lambda x ="about": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Add Admin", "left_icon": "acc.png", "height": dp(56),
                                                "on_release": lambda x ="addAdmin": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Staff Details", "left_icon": "staff.png", "height": dp(56),
                                                "on_release": lambda x="Staff Details": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Logout", "left_icon": "logout.jpg", "height": dp(56),
                                                "on_release": lambda x ="login": self.menu_callback(x, menu)},
        ]
        menu = MDDropdownMenu(
            caller=instance,
            items=menu_items,
            width_mult=4,
        )
        menu.open()

    def open_menu_for_books(self, instance):
        # Create a dropdown menu
        menu_items = [
            {"viewclass": "Item", "text": "Show Books", "left_icon": "bookIcon.png", "height": dp(56),
                                                "on_release": lambda x = "booksDisplay": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Add Book", "left_icon": "addIcon.png", "height": dp(56),
                                                "on_release": lambda x = "AddBookPopup": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Remove Book", "left_icon": "removeIcon.png", "height": dp(56),
                                                "on_release": lambda x = "RemoveBookPopup": self.menu_callback(x, menu)},

            {"viewclass": "Item", "text": "Issue Book", "left_icon": "IssueBook.png", "height": dp(56),
                                                "on_release": lambda x = "IssueBookPopup": self.menu_callback(x, menu)}
        ]
        menu = MDDropdownMenu(
            caller=instance,
            items=menu_items,
            width_mult=4,
        )
        menu.open()

    def menu_callback(self, name, menu):
        menu.dismiss()
        if name == "booksDisplay":
            sm.current = name

        elif name == "about":
            sm.current = name

        elif name == "addAdmin":
            sm.current = name

        elif name == "Staff Details":
            staff = StaffPopup()
            staff.open()

        elif name == "login":
            sm.current = name

        elif name == "AddBookPopup":
            addBookPopup = AddBookPopup(title='Add Book', size_hint=(None, None), size=('300dp', '400dp'))
            addBookPopup.open()

        elif name == "RemoveBookPopup":
            removeBookPopup = RemoveBookPopup()
            removeBookPopup.open()

        elif name == "IssueBookPopup":
            issueBookPopup = IssuePopup()
            issueBookPopup.open()

class PopupContent(BoxLayout):
    def __init__(self, **kwargs):
        super(PopupContent, self).__init__(**kwargs)
        self.ids['B1'].bind(on_release = self.update_book)
        self.ids['B3'].bind(on_release=self.rollBack)

    def update_book(self,instance):
        if self.ids['B1'].text == 'Update':
            Snackbar(text=(" "*40)+"Enter updated values in appeared text-boxes and press enter").open()
            self.num_copy = self.ids['5']
            self.num_copy_index = list(self.ids).index('5')
            self.shelf = self.ids['6']
            self.shelf_index = list(self.ids).index('6')
            self.remove_widget(self.num_copy)
            self.remove_widget(self.shelf)
            self.update_num_copy = TextInput(hint_text = 'Enter Updated No. of copies', multiline = False)
            self.update_shelf = TextInput(hint_text = 'Enter Updated shelf location', multiline = False)
            self.add_widget(self.update_num_copy, index=-(self.num_copy_index))
            self.add_widget(self.update_shelf, index=-(self.shelf_index))
            self.ids['B1'].text = 'Enter'
            self.ids['B2'].disabled = True
            self.ids['B1'].unbind(on_release=self.update_book)
            self.ids['B1'].bind(on_release = self.update_book_continued)

    def update_book_continued(self,instance):
        if self.ids['B1'].text == 'Enter':
            book_id = int(self.ids['1'].text[-1])
            updated_num_copy = self.update_num_copy.text
            updated_shelf = self.update_shelf.text
            if updated_num_copy != "" or updated_shelf != "":
                updated_num_copy = int(updated_num_copy)
                status = update_book(book_id=book_id, new_copies=updated_num_copy, new_location=updated_shelf)
                if status == "Book updated successfully":
                    self.num_copy.text = updated_num_copy
                    self.shelf.text = updated_shelf
                    sbar = Snackbar(text=(" " * 70) + status).open()
                else:
                    sbar = Snackbar(text=(" " * 50) + status).open()
            else:
                Snackbar(text=(" "*70)+"Values couldn't be updated!!!").open()

        self.rollBack(None)

    def rollBack(self, instance):
        try:
            self.remove_widget(self.update_num_copy)
            self.remove_widget(self.update_shelf)
            self.add_widget(self.num_copy, index=-(self.num_copy_index))
            self.add_widget(self.shelf, index=-(self.shelf_index))
            self.ids['B1'].text = 'Update'
            self.ids['B1'].unbind(on_release=self.update_book_continued)
            self.ids['B1'].bind(on_release=self.update_book)
            self.ids['B2'].disabled = False

        except:
            pass

class StaffPopup(Popup):
    def __init__(self, **kwargs):
        super(StaffPopup, self).__init__(**kwargs)
        self.title = 'Manage Staff'
        self.size_hint = (0.4, 0.4)

        self.layout = BoxLayout(orientation='vertical', spacing = 10)
        # label = Label(text='Book removed successfully!!!')
        self.search_staff = TextInput(hint_text="Search by Staff ID or Name:", size_hint= (1,None), size= ('100dp','50dp'), multiline=False)
        self.search_staff.bind(on_text_validate=self.searchStaff)
        add_button = Button(text='Add Staff', size_hint=(1, None), size= ('100dp','50dp'))
        add_button.bind(on_release=self.addStaff)
        self.close_button = Button(text='Close', size_hint=(1, None), size= ('100dp','50dp'), color = 'red')
        self.close_button.bind(on_release=self.dismiss)

        self.layout.add_widget(self.search_staff)
        self.layout.add_widget(add_button)
        self.layout.add_widget(self.close_button)
        self.content = self.layout

    def searchStaff(self, instance):
        gettext = self.search_staff.text
        if gettext.isdigit():
            gettext = int(gettext)
        staff = search_staff(gettext)
        if staff:
            self.layout.clear_widgets()
            self.size_hint = (None,None)
            self.size = ('300dp', '400dp')
            labl1 = Label(text=f'Staff ID: {staff[0]}')
            labl2 = Label(text=f'Name: {staff[1]}')
            self.labl3 = Label(text=f'Designation: {staff[2]}')
            self.update_button = Button(text='Update Staff', size_hint=(1, None), size= ('100dp','50dp'))
            self.update_button.bind(on_release=lambda x:self.updateStaff(staff[0]))
            self.delete_button = Button(text='Delete Staff', size_hint=(1, None), size= ('100dp','50dp'))
            self.delete_button.bind(on_release=lambda x:self.deleteStaff(staff[0]))

            self.layout.add_widget(labl1)
            self.layout.add_widget(labl2)
            self.layout.add_widget(self.labl3)
            self.layout.add_widget(self.update_button)
            self.layout.add_widget(self.delete_button)
            self.layout.add_widget(self.close_button)

        else:
            Snackbar(text=(' '*60)+"No Staff With This ID or Name!!!").open()

    def updateStaff(self, staffID):
        self.layout.remove_widget(self.layout.children[3])
        self.layout.remove_widget(self.layout.children[2])
        self.layout.remove_widget(self.layout.children[1])
        self.new_desg = TextInput(hint_text="Enter Updated designation:", size_hint= (1,None), size= ('100dp','50dp'), multiline=False)
        self.new_desg.bind(on_text_validate=lambda x:self.updateStaffCont(staffID))
        self.layout.add_widget(self.new_desg,index=1)
        labl = Label(text="Enter the updated value in above Textbox and press enter key", size=(self.width * 0.8, self.height * 0.2),
            text_size=(self.width * 0.8, None))
        self.layout.add_widget(labl,index=1)

    def updateStaffCont(self, staffID):
        new_des = self.new_desg.text
        if new_des != "":
            status = update_staff(staff_id=staffID, new_designation=new_des)
        else:
            status = "Designation can not be empty"
        self.layout.remove_widget(self.layout.children[2])
        self.layout.remove_widget(self.layout.children[1])
        self.layout.add_widget(self.labl3,1)
        self.layout.add_widget(self.update_button,1)
        self.layout.add_widget(self.delete_button,1)
        if status == "staff details updated successfully":
            self.labl3.text = new_des
        Snackbar(text=(" "*60)+status).open()

    def deleteStaff(self, staffID):
        status = delete_staff(staffID)
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=status, size=(self.width * 0.8, self.height * 0.2),
            text_size=(self.width * 0.8, None)))
        self.layout.add_widget(self.close_button)
        self.size = ('300dp','200dp')

    def addStaff(self, instance):
        self.layout.clear_widgets()
        self.size_hint=(None,None)
        self.size = ('300dp','350dp')
        newStaffID = generateStaffID()
        self.idInp = TextInput(text="Staff ID: "+str(newStaffID), size_hint= (1,None), size= ('100dp','50dp'), multiline=False, disabled=True)
        self.nameInp = TextInput(hint_text="Enter Name: ", size_hint=(1, None), size=('100dp', '50dp'), multiline=False)
        self.desigInp = TextInput(hint_text="Enter Designation: ", size_hint=(1, None), size=('100dp', '50dp'), multiline=False)
        enter = Button(text="Enter", size_hint=(1, None), size=('100dp', '50dp'), on_release=self.addStaffCont)

        self.layout.add_widget(self.idInp)
        self.layout.add_widget(self.nameInp)
        self.layout.add_widget(self.desigInp)
        self.layout.add_widget(enter)
        self.layout.add_widget(self.close_button)


    def addStaffCont(self, instance):
        name = self.nameInp.text
        desg = self.desigInp.text

        status = insert_staff(staff_name=name, designation=desg)
        self.layout.clear_widgets()

        self.layout.add_widget(Label(text=status, size=(self.width * 0.8, self.height * 0.2),
            text_size=(self.width * 0.8, None)))
        self.layout.add_widget(self.close_button)
        self.size = ('300dp','200dp')

class IssuePopup(Popup):
    def __init__(self, **kwargs):
        super(IssuePopup, self).__init__(**kwargs)
        self.title = 'Issue Book'
        self.size_hint = (None, None)
        self.size = ('300dp', '300dp')

        # Main container layout
        self.main_layout = BoxLayout(orientation='vertical', spacing='5dp')

        self.text_input = TextInput(hint_text="Book ID",size_hint=(1, None), size=('50dp', '50dp'), pos_hint = {'y': 0}, multiline=False )
        self.main_layout.add_widget(self.text_input)

        # First text field
        self.text_input1 = TextInput(hint_text="Member ID", size_hint=(1, None), size=('50dp', '50dp'), multiline=False)
        self.main_layout.add_widget(self.text_input1)

        # Second text field with current date
        self.text_input2 = TextInput(hint_text="Issue Date", disabled=True, size_hint=(1, None), size=('50dp', '50dp'))
        self.main_layout.add_widget(self.text_input2)

        # Third text field with date after 7 days
        self.text_input3 = TextInput(disabled=True, size_hint=(1, None), size=('50dp', '50dp'))
        self.main_layout.add_widget(self.text_input3)

        # Set current date and date after 7 days
        today = date.today()
        self.text_input2.text = 'Issue Date: ' + str(today)
        self.text_input3.text = 'Due Date: ' + str(today + timedelta(days=7))

        # Button layout
        self.button_layout = BoxLayout(spacing='10dp', size_hint=(1, None), height='48dp')

        # Confirm button
        button1 = Button(text='Confirm', size_hint=(0.1, 0.8), background_color='blue')
        button1.bind(on_release=self.confirmButton)
        self.button_layout.add_widget(button1)

        # Cancel button
        button2 = Button(text='Cancel', size_hint=(0.1, 0.8), background_color='red', on_release=self.dismiss)
        self.button_layout.add_widget(button2)


        self.main_layout.add_widget(self.button_layout)

        # Final layout with main and additional layouts
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.main_layout)

        self.content = self.layout

    def confirmButton(self, x):
        self.text_input.disabled = True
        self.text_input1.disabled = True
        bid = self.text_input.text
        mid = self.text_input1.text

        if bid.isdigit() and mid.isdigit():
            bid, mid = int(bid), int(mid)
            book = search_books(bid)
            member = search_member(mid)
            if book and member:
                status = borrow_book(member_id=mid, book_id=bid, book_fee=0)

        else:
            status = "Invalid Book ID or Member ID"

        lLayout = BoxLayout(orientation = 'vertical',spacing='10dp', size_hint=(1, 0.8), height='60dp', padding = 10)
        label = Label(text=status, size_hint= (1,None), size=('50dp', '50dp'))
        lLayout.add_widget(label)
        back = Button(text = 'Go Back', color = 'red', size_hint= (1,None), size=('50dp', '50dp'), on_release = self.dismiss)
        lLayout.add_widget(back)

        self.main_layout.remove_widget(self.main_layout.children[0])
        self.layout.add_widget(lLayout)
        self.size = (self.layout.size[0] + 20, self.layout.size[1] + 150)

class DisplayBooks(MDScreen):
    def __init__(self, **kwargs):
        super(DisplayBooks, self).__init__(**kwargs)

        self.book_list = list(view_all_book())

        self.orientation = 'vertical'
        bgImage = Image(source="bookBg.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(bgImage)

        self.main_layout = BoxLayout(orientation='vertical', padding = 10)

        # Create the BoxLayout at the top
        self.top_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50,
                                    pos_hint={'x': 0.01, 'top': 0.98})

        # Create the "Go Back" button
        self.go_back_button = Button(text="Go Back", size_hint=(None, None), size=('100dp', '50dp'),on_release = self.goto)
        self.top_layout.add_widget(self.go_back_button)

        # Create the "Refresh" button
        self.refresh_button = Button(text="Refresh", size_hint=(None, None), size=('100dp', '50dp'))
        self.top_layout.add_widget(self.refresh_button)

        self.searchBook = TextInput(hint_text = "Search Book By Id", size_hint=(None, None), size=('300dp', '50dp'),
                                    multiline = False)
        self.top_layout.add_widget(self.searchBook)
        self.searchBook.bind(on_text_validate = self.searchBookFunc)
        # Add the top layout to the main layout
        self.main_layout.add_widget(self.top_layout)

        # Create a ScrollView
        self.scroll_view = ScrollView()

        # Create a BoxLayout to hold the content
        self.content_layout = GridLayout(size_hint=(1, None), spacing=10, rows=50, cols=2)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        # Add the content layout to the ScrollView
        self.scroll_view.add_widget(self.content_layout)

        # Add the ScrollView to the main layout
        self.main_layout.add_widget(self.scroll_view)

        # Add the main layout to the screen
        self.add_widget(self.main_layout)

        # Bind the refresh method to the refresh button
        self.refresh_button.bind(on_release=self.refresh)

        # Load initial content
        self.load_content()

    def searchBookFunc(self, instance):
        bId = self.searchBook.text
        if bId.isdigit():
            bId = int(self.searchBook.text)
        book = search_books(bId)
        if book:
            self.show_popup(bId)

        else:
            popup = Popup(title='Book ID Error', size_hint=(None, None), size=('300dp', '200dp'))
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text="No book found!!!"))
            layout.add_widget(Button(text="Close", color = "red", on_release = popup.dismiss))
            setattr(popup,"content",layout)
            popup.open()
        self.searchBook.text = ""

    def load_content(self):
        # Clear existing content
        self.content_layout.clear_widgets()

        # Add some labels to the content layout
        for i in range(len(self.book_list)):
            label = Label(
                text=f'[ref=link][u][b]Book ID: {self.book_list[i][0]}  Name: {self.book_list[i][1]}[/b][/u][/ref]',
                markup=True,
                size_hint=(1, None),
                height=40,
                on_ref_press=lambda label, i: self.show_popup(label.id)
            )
            setattr(label, 'id', str(self.book_list[i][0]))
            self.content_layout.add_widget(label)

    def refresh(self, instance):
        self.load_content()

    def goto(self, instance):
        sm.current = "portal"

    content = PopupContent()
    popup = Popup(title='Book Information', content=content, size_hint=(None, None), size=('300dp', '400dp'))

    def show_popup(self, labelID):
        l = search_books(labelID)
        for i in range(1,7):
            labl = self.content.ids[str(i)]
            labl.text = labelStartTags[i-1] + str(l[i-1])
        self.popup.open()

    # def show_deletion_popup(self):
    #     self.removeTuple()
    #     popup = DeletePopup()
    #     popup.open()

    def show_issue_popup(self, bid):
        popup = IssuePopup()
        popup.text_input.text = bid
        popup.text_input.disabled = True
        popup.open()

    def close_popup(self):
        self.popup.dismiss()

    def removeTuple(self):
        formTuple = ()
        for i in range(1,6):
            labl = self.content.ids[str(i)]
            formTuple += labl.text.split(':')[1][1:],
        self.book_list.remove(formTuple)
        self.refresh("instance")

# Define the app
class MyApp(MDApp):

    def build(self):
        # Create the screens
        welcome_screen = WelcomeScreen(name='welcome')
        login_screen = LoginScreen(name="login")
        about_screen = AboutScreen(name="about")
        addAdmin_screen = AddAdmin(name="addAdmin")
        portal_screen = Portal(name="portal")
        book_display = DisplayBooks(name="booksDisplay")
        member_screen = MemberScreen(name="member")
        help_screen = HelpScreen(name="help")

        member_screen.go_back.bind(on_ref_press= lambda x,y: self.goto())
        about_screen.return_button.bind(on_release = lambda x: self.goto())
        help_screen.return_button.bind(on_release=lambda x: self.goto())

        # Add the screens to the screen manager
        sm.add_widget(welcome_screen)
        sm.add_widget(about_screen)
        sm.add_widget(login_screen)
        sm.add_widget(addAdmin_screen)
        sm.add_widget(portal_screen)
        sm.add_widget(book_display)
        sm.add_widget(member_screen)
        sm.add_widget(help_screen)

        # Set the welcome screen as the current screen
        sm.current = "welcome"

        return sm

    def goto(self, name = "portal"):
        sm.current = name

# Run the app
MyApp().run()
