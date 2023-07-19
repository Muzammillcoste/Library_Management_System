from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.snackbar import Snackbar
from kivy.uix.popup import Popup
from oracle_test import view_all_members, insert_member, update_member, delete_member, search_member,\
    borrow_book_history, borrow_book_current, return_borrow_book

member_info_starting_tags = ['Member ID: ', 'Name: ', 'Address: ', 'Contact: ', 'E-mail: ']

class MemberScreen(Screen):
    memID = None
    def __init__(self, **kwargs):
        super(MemberScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        bgImage = Image(source="mem_bg.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(bgImage)
        self.member_data = list(view_all_members())
        self.main_layout = BoxLayout()
        # Create the BoxLayout for the top 1/3 portion of the screen
        self.top_layout = BoxLayout(orientation='vertical', size_hint=(None, 1), size=(300, 300), padding=10, spacing=10)

        # Add a TextInput field
        self.text_input = TextInput(hint_text="Search Member", size_hint=(1,None), size=("1dp","50dp"), multiline = False)
        self.top_layout.add_widget(self.text_input)
        self.text_input.bind(on_text_validate=self.searchMemFunc)

        # Add 5 hyperlink labels
        add = Label(text=f'[ref=link][u][b]Add Member[/b][/u][/ref]', markup=True, font_size="24sp",
                    on_ref_press = self.addMem)
        self.top_layout.add_widget(add)

        self.remove = Label(text=f'[ref=link][u][b]Remove Member[/b][/u][/ref]', markup=True, font_size="24sp",
                       on_ref_press = lambda x,y: self.removeUpdateMem(None,None,4))
        self.top_layout.add_widget(self.remove)

        self.update = Label(text=f'[ref=link][u][b]Update Member Info[/b][/u][/ref]', markup=True, font_size="24sp",
                       on_ref_press = lambda x,y: self.removeUpdateMem(None,None,3))
        self.top_layout.add_widget(self.update)

        self.return_book = Label(text=f'[ref=link][u][b]Return Book[/b][/u][/ref]', markup=True, font_size="24sp",
                        on_ref_press = lambda x,y: self.removeUpdateMem(None,None,2))
        self.top_layout.add_widget(self.return_book)

        self.refresh = Label(text=f'[ref=link][u][b]Refresh[/b][/u][/ref]', markup=True, font_size="24sp",
                       on_ref_press = self.refreshFunc)
        self.top_layout.add_widget(self.refresh)

        self.go_back = Label(text=f'[ref=link][u][b]Go Back[/b][/u][/ref]', markup=True, font_size="24sp")
        self.top_layout.add_widget(self.go_back)

        # Create a ScrollView
        scroll_view = ScrollView(top = 100)
        self.complete = BoxLayout(orientation="vertical")
        bar_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50,
                                    pos_hint={'x': 0.01, 'top': 0.98})
        bar_layout.add_widget(Label(text=f'[b]Showing all members, scroll down to view more[/b]',
                                    markup=True,font_size="20sp"))

        self.content_layout = GridLayout(size_hint=(1, None), spacing=10, padding = 10, rows=100, cols=1)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        scroll_view.add_widget(self.content_layout)
        self.complete.add_widget(bar_layout)
        self.complete.add_widget(scroll_view)
        # Add the layouts to the main BoxLayout
        self.main_layout.add_widget(self.top_layout)
        self.main_layout.add_widget(self.complete)

        self.add_widget(self.main_layout)
        self.load_content()

    def refreshFunc(self,instance1,instance2):
        self.member_data = list(view_all_members())
        self.load_content()
        self.restoreLabel()

    def removeUpdateMem(self, instance1, instance2, index):
        if index == 4:
            if isinstance(self.top_layout.children[3], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[3])
                self.top_layout.add_widget(self.update, 3)
            elif isinstance(self.top_layout.children[2], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[2])
                self.top_layout.add_widget(self.return_book, 2)
            self.top_layout.remove_widget(self.remove)
        elif index == 3:
            if isinstance(self.top_layout.children[4], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[4])
                self.top_layout.add_widget(self.remove, 4)
            elif isinstance(self.top_layout.children[2], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[2])
                self.top_layout.add_widget(self.return_book, 2)
            self.top_layout.remove_widget(self.update)
        elif index == 2:
            if isinstance(self.top_layout.children[4], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[4])
                self.top_layout.add_widget(self.remove, 4)
            elif isinstance(self.top_layout.children[3], TextInput):
                self.top_layout.remove_widget(self.top_layout.children[3])
                self.top_layout.add_widget(self.update, 3)
            self.top_layout.remove_widget(self.return_book)

        self.memID = TextInput(hint_text="Enter Member ID", size_hint=(1, None), size=("1dp", "50dp"), multiline=False)
        self.memID.bind(on_text_validate=lambda x=None :self.removeUpdateMemCont(x,index))
        self.top_layout.add_widget(self.memID, index)

    def removeUpdateMemCont(self, instance, index):
        getMemId = self.memID.text
        if getMemId.isdigit():
            getMemId = int(getMemId)
        m = search_member(getMemId)

        if m:
            if index == 4:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.remove, 4)
                txt = "Member exists"
                btn = Button(text='Remove', color='blue', size_hint = (1, None), size = ("150dp", "50dp"),
                             on_release = lambda x:self.removeMemEnd(txt, m))
                self.show_attr(getMemId, btn)

            elif index == 3:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.update, 3)
                self.addMem(None,None,memInfoTuple=m)

            elif index == 2:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.return_book, 2)
                self.historyLabelFunc(status="Current",memId=getMemId)

        else:
            self.removeMemEnd(None, None)

    def removeMemEnd(self, txt, memtuple):
        self.restoreLabel()
        if txt == None:
            status = "No member with this ID"
        elif memtuple != None:
            status = delete_member(memtuple[0])
            if status == "Member deleted successfully!":
                self.member_data.remove(memtuple)
                self.load_content()
        self.popup = Popup(title="Messsage", size_hint=(None, None), size=(400, 200))
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=status))
        layout.add_widget(Button(text="Close", size_hint=(None, None), size=("150dp", "50dp"), pos_hint={'x': 0.3},
                                 on_release=self.popup.dismiss))
        self.popup.content = layout
        self.popup.open()

    def addMem(self,instance1, instance2, memInfoTuple = None):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.top_layout)
        self.restoreLabel()

        self.newLayout = BoxLayout(orientation="vertical", spacing = 10, padding = 70)

        self.newLayout.add_widget(Label(text="[b]Provide/Update following information[/b]", markup = True, color = 'cyan',font_size="20sp" ))

        self.idInp = MDTextField(hint_text="Member ID",text = str(int(self.member_data[-1][0])+1), multiline = False, mode = 'fill',
                               size_hint= (None, None), size=('300dp', '50dp'), disabled = True)
        self.fnameInp = MDTextField(hint_text="First Name", multiline = False, size_hint= (None, None), size=('300dp', '50dp'), mode = 'fill')
        self.lnameInp = MDTextField(hint_text="Last Name", multiline = False, size_hint= (None, None), size=('300dp', '50dp'), mode = 'fill')
        self.addressInp = MDTextField(hint_text="Resedential Address", size_hint= (None, None), size=('300dp', '50dp'), mode = 'fill')
        self.mailInp = MDTextField(hint_text="Email Address", size_hint= (None, None), size=('300dp', '50dp'), mode = 'fill')
        self.contactInp = MDTextField(hint_text="Contact Number", multiline = False, size_hint= (None, None), size=('300dp', '50dp'), mode = 'fill')

        self.newLayout.add_widget(self.idInp)
        self.newLayout.add_widget(self.fnameInp)
        self.newLayout.add_widget(self.lnameInp)
        self.newLayout.add_widget(self.addressInp)
        self.newLayout.add_widget(self.mailInp)
        self.newLayout.add_widget(self.contactInp)

        if memInfoTuple != None:
            self.idInp.text = str(memInfoTuple[0])
            self.fnameInp.text = memInfoTuple[1]
            self.fnameInp.disabled = True
            self.lnameInp.text = memInfoTuple[2]
            self.lnameInp.disabled = True
            self.addressInp.text = memInfoTuple[3]
            self.mailInp.text = memInfoTuple[5]
            self.contactInp.text = str(memInfoTuple[4])

        bLayout = BoxLayout(spacing = 100)
        bLayout.add_widget(Button(text="Enter", background_color = 'blue',size_hint= (None, None), size=('100dp', '50dp'),
                                  on_release = lambda x:self.addBtn(None,memUpdate=memInfoTuple)))
        bLayout.add_widget(Button(text="cancel", background_color = 'red',size_hint= (None, None), size=('100dp', '50dp'),
                                  on_release= self.restore))
        self.newLayout.add_widget(bLayout)

        self.main_layout.add_widget(self.newLayout)

    def restore(self, instance):
        self.main_layout.remove_widget(self.newLayout)
        self.main_layout.add_widget(self.complete)
        self.load_content()

    def restoreLabel(self):
        if self.memID in self.top_layout.children:
            inx = self.top_layout.children.index(self.memID)
            if inx == 2:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.return_book, 2)
            elif inx == 3:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.update, 3)

            elif inx == 4:
                self.top_layout.remove_widget(self.memID)
                self.top_layout.add_widget(self.remove, 4)

    def addBtn(self, instance, memUpdate = None):
        id = int(self.idInp.text)
        fname = self.fnameInp.text
        lname = self.lnameInp.text
        address = self.addressInp.text
        email = self.mailInp.text
        contact = self.contactInp.text
        if contact.isdigit():
            contact = int(contact)

        if memUpdate == None:
            if fname != "" or lname != "" or address != "" or email != "" or contact != "":
                status = insert_member(f_name=fname, l_name=lname, email=email, contact_no=contact, address=address)
            else:
                status = "One or more fields missing"
        elif memUpdate != None:
            if address != "" or email != "" or contact != "":
                status = update_member(member_id=id, address=address, contact_number=contact, email=email)
            else:
                status = "One or more fields missing"
        self.member_data = list(view_all_members())
        self.load_content()

        popup = Popup(title="Confirmation", size_hint = (None, None), size = (400, 200))
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=status))
        layout.add_widget(Button(text="Close", size_hint = (None, None), size = ("150dp", "50dp"), pos_hint = {'x':0.3},
                                 on_release = popup.dismiss))
        popup.content = layout
        popup.open()
        self.restore("instance")

    def load_content(self):
        # Clear existing content
        self.content_layout.clear_widgets()

        # Add some labels to the content layout
        for i in range(len(self.member_data)):
            label = Label(
                text=f'[ref=link][u][b]Member ID: {self.member_data[i][0]}  Name: {self.member_data[i][1]+" "+self.member_data[i][2]}[/b][/u][/ref]',
                markup=True,
                size_hint=(1, None),
                height=40,
                color = "cyan",
                on_ref_press=lambda label, i: self.show_attr(label.id)
            )
            setattr(label, 'id', str(self.member_data[i][0]))
            self.content_layout.add_widget(label)

    def show_attr(self, memID, arg = None):
        self.restoreLabel()
        attrPopup = Popup(title="Member Info", size_hint=(None, None), size=('300dp','500dp'))
        layout = BoxLayout(orientation="vertical")
        layout.clear_widgets()
        m = search_member(int(memID))
        for i in range(5):
            if i == 0:
                labl = Label(text=f'{member_info_starting_tags[i]} {m[i]}')
            elif i == 1:
                labl = Label(text=f'{member_info_starting_tags[i]} {m[i]+" "+m[i+1]}')
            else:
                labl = Label(text=f'{member_info_starting_tags[i]} {m[i+1]}')
            layout.add_widget(labl)

        labl1 = Label(text=f'[ref=link][u]Show Borrow History[/u][/ref]', color = 'cyan', markup = True,
                      on_ref_press= lambda x,y:self.historyLabelFunc(status="History",memId=memID))
        layout.add_widget(labl1)
        labl2 = Label(text=f'[ref=link][u]Show Borrowed Books[/u][/ref]', color = 'cyan', markup = True,
                      on_ref_press= lambda x,y:self.historyLabelFunc(status="Current",memId=memID))
        layout.add_widget(labl2)

        blayout = BoxLayout()
        if isinstance(arg,Button):
            arg.bind(on_release = attrPopup.dismiss)
            blayout.add_widget(arg)
        blayout.add_widget(Button(text="close", color='red', size_hint = (1, None), size = ("150dp", "50dp"),
                                  on_release= attrPopup.dismiss))

        layout.add_widget(blayout)

        attrPopup.content = layout
        attrPopup.open()

    def historyLabelFunc(self, status, memId, bInfo = None):
        hist = bInfo
        if status == "History":
            history = borrow_book_history(memId)
        elif status == "Current":
            history = borrow_book_current(memId)

        if bInfo == None:
            if history:
                hist = history[0]

        if hist:
            historyPopup = Popup(title="Books Borrowed", size_hint=(None, None), size=('300dp','500dp'))
            layout = BoxLayout(orientation = 'vertical')
            labl1 = Label(text='Book ID: ' + str(hist[0]))
            layout.add_widget(labl1)
            labl2 = Label(text='Name: ' + str(hist[1]))
            layout.add_widget(labl2)
            labl3 = Label(text='Issue Date: ' + str(hist[2]))
            layout.add_widget(labl3)
            labl4 = Label(text='Due Date: ' + str(hist[3]))
            layout.add_widget(labl4)
            try:
                labl5 = Label(text='Return Date: ' + str(hist[4]))
                layout.add_widget(labl5)
            except:
                rbtn = Button(text="Return Book",size_hint = (1, None), size = ('100dp','50dp'), color='blue',
                              on_release = historyPopup.dismiss)
                rbtn.bind(on_release=lambda x:self.rbtnFunc(hist[0],memId))
                layout.add_widget(rbtn)

            pinx = history.index(hist) - 1
            ninx = history.index(hist) + 1

            bLayout = BoxLayout()
            pre = Button(text="previous", size_hint = (1, None), size = ('100dp','50dp'),
                         on_release=historyPopup.dismiss)
            pre.bind(on_release=lambda x:self.historyLabelFunc(status=status, memId=memId, bInfo=history[pinx]))
            if pinx < 0:
                pre.disabled = True
            bLayout.add_widget(pre)
            close = Button(text="close", color='red',size_hint = (1, None), size = ('100dp','50dp'), on_release=historyPopup.dismiss)
            bLayout.add_widget(close)
            nxt = Button(text="next", size_hint = (1, None), size = ('100dp','50dp'),
                         on_release=historyPopup.dismiss)
            nxt.bind(on_release=lambda x:self.historyLabelFunc(status=status, memId=memId, bInfo=history[ninx]))
            if ninx > (len(history) - 1):
                nxt.disabled = True
            bLayout.add_widget(nxt)
            layout.add_widget(bLayout)
            historyPopup.open()
            historyPopup.content = layout

        else:
            Snackbar(text=(" "*80) + "No Records Found").open()

    def rbtnFunc(self, bid, mid):
        status = return_borrow_book(member_id=mid,book_id=bid )
        Snackbar(text=(" "*70)+status).open

    def searchMemFunc(self, instance):
        self.restoreLabel()
        mId = self.text_input.text
        if mId.isdigit():
            mId = int(self.text_input.text)
        mem = search_member(mId)
        if mem:
            self.show_attr(mId)

        else:
            popup = Popup(title='Member ID Error', size_hint=(None, None), size=('300dp', '200dp'))
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text="No Member found!!!"))
            layout.add_widget(Button(text="Close", color = "red", on_release = popup.dismiss))
            setattr(popup,"content",layout)
            popup.open()
        self.text_input.text = ""

class MyApp(MDApp):
    def build(self):
        return MemberScreen()

if __name__ == '__main__':
    MyApp().run()
