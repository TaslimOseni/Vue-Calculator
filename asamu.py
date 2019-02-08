import tkinter
import json
import os
import tkinter.messagebox as tm
import json 

def load_data():
    global restaurants_order
    global DATA
    with open("restaurants.json", 'rb') as myfile:
        text = myfile.read().decode('utf8')
        DATA = json.loads(text)
        restaurants_order = list(DATA["restaurants"].keys())

def bubbleSort():
    load_data()
    for i in range(len(restaurants_order)):
        for j in range(0, len(restaurants_order)-i-1):
            if restaurants_order[j] > restaurants_order[j+1]:
                restaurants_order[j], restaurants_order[j+1] = restaurants_order[j+1], restaurants_order[j]

    for i in range(len(restaurants_order)):
        print (restaurants_order[i])
        
#prints the information of each resturant when the it's button is clicked 
class InfoFrame:
    def __init__(self, root, info):
        print(info)
        self.root = tkinter.Toplevel(root)
        self.root.title("Information")
        
        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

        self.entry_1 = tkinter.Entry(self.frame)
        self.entry_1.grid(row=0, column=1)
        self.label_1 = tkinter.Label(self.frame, text="Phone number")
        self.label_1.grid(row=0, sticky=tkinter.E)
        self.entry_1.insert('end', info["number"])

        self.entry_2 = tkinter.Entry(self.frame)
        self.entry_2.grid(row=1, column=1)
        self.label_2 = tkinter.Label(self.frame, text="Address")
        self.label_2.grid(row=1, sticky=tkinter.E)
        self.entry_2.insert('end', info["address"])

        self.entry_3 = tkinter.Text(self.frame, height=5, width=30)
        self.entry_3.grid(row=2, column=1)
        self.label_3 = tkinter.Label(self.frame, text="Menu")
        self.label_3.grid(row=2, sticky=tkinter.E)

        product_names = list(info["menu"].keys())
        product_names.sort()

        menu = info["menu"]
        product_price = list(menu.values())
        product_price.sort()
        
        for product_name in product_names:
            self.entry_3.insert('end', product_name)
            self.entry_3.insert('end', ' --- ')
            self.entry_3.insert('end', menu[product_name])
            self.entry_3.insert('end', '\n')
        
        self.logbtn = tkinter.Button(self.frame, text="OK", command = self.root.destroy)
        self.logbtn.grid(columnspan=2)

        self.root.mainloop() 

class RestaurantFrame:
    def __init__(self, root):
        load_data() # Read in JSON data

        self.restaurants = DATA["restaurants"]

        # Create the window to show the restaurant buttons
        self.root = tkinter.Toplevel(root)      
        self.root.title("Restaurant choices")
        tkinter.Label(self.root, text="Please click a restaurant below").pack()

        frame = tkinter.Frame(self.root)
        frame.pack()

        label_1 = tkinter.Label(frame, text="Search for:")
        label_1.grid(row=0, sticky=tkinter.E)
        self.entry_1 = tkinter.Entry(frame)
        self.entry_1.grid(row=0, column=1)

        search = tkinter.Button(frame, text="Search", command = self.on_search)
        search.grid(row=0, column=2)
        
        sort = tkinter.Button(frame, text="Sort", command = bubbleSort)
        sort.grid(row=1, column=0)
        
        self.restaurant_frame = None
        self.show_restaurants("")

        
    def on_search(self):
        search_term = self.entry_1.get()
        self.show_restaurants(search_term)
                    

    def show_restaurants(self, search_term):
        if self.restaurant_frame is not None:
            self.restaurant_frame.pack_forget()
        self.restaurant_frame = tkinter.Frame(self.root)
        self.restaurant_frame.pack()

        # Create a button for each restaurant in the data file.
        for name, info in self.restaurants.items():
            is_match = False
            info = self.restaurants[name]
            menu = info["menu"]

            if search_term.upper() in name.upper():
                is_match = True
            else:
                for menu_item in menu.keys():
                    if search_term.upper() in menu_item.upper():
                        is_match = True
 
            if is_match:
                def on_click(info=info): InfoFrame(self.root, info)
                button = tkinter.Button(self.restaurant_frame, text = name, command = on_click)
                button.pack()

class LoginFrame:
    def __init__(self):
        self.root = tkinter.Tk()
        
        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

        self.entry_1 = tkinter.Entry(self.frame)
        self.entry_1.grid(row=0, column=1)
        self.label_1 = tkinter.Label(self.frame, text="Username")
        self.label_1.grid(row=0, sticky=tkinter.E)

        self.entry_2 = tkinter.Entry(self.frame, show="*")
        self.entry_2.grid(row=1, column=1)
        self.label_2 = tkinter.Label(self.frame, text="Password")
        self.label_2.grid(row=1, sticky=tkinter.E)
        
        self.checkbox = tkinter.Checkbutton(self.frame, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)
        
        self.logbtn = tkinter.Button(self.frame, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.root.mainloop()

        
    def _login_btn_clickked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        if username == "" and password == "":
            RestaurantFrame(self.root)
        else:
            tm.showerror("Login error", "Incorrect username or password")

LoginFrame() 
