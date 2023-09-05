"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from place import Place
from placecollection import PlaceCollection
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class TravelTrackerApp(App):
    counter = ObjectProperty(None)
    def build(self):
        self.root = Builder.load_file("app.kv")
        self.custom = CustomClass()
        return self.root
    def on_stop(self):
        app = App.get_running_app()
        custom = app.root.ids.custom_class
        custom.collection.save_places("places.csv")
        return super().on_stop()
    

class CustomClass(BoxLayout):
    collection = PlaceCollection()
    def __init__(self, **kwargs):
        super(CustomClass, self).__init__(**kwargs)
        self.collection.load_places("places.csv")
        self.build_places()

    def build_places(self):
        self.clear_widgets()
        self.add_widget(Label(text = f"Places To Visit: {self.collection.get_number_of_unvisited()}", size_hint_y= 0.2))
        i = 0
        for place in self.collection.places:
            temp = Button(text = place.__str__())
            temp.id = f"{i}"
            temp.bind(on_release=self.on_button_release)
            if place.is_visited == False:
                temp.background_color = "darkgreen"
                self.add_widget(temp)
            else:
                self.add_widget(temp)
            i += 1

    def on_button_release(self, button):
        app = App.get_running_app()
        message = app.root.ids.message
        self.collection.places[int(button.id)].is_visited = not self.collection.places[int(button.id)].is_visited
        if self.collection.places[int(button.id)].is_visited == False:
            if self.collection.places[int(button.id)].isImp() == True:
                message.text = f"You need to visit {self.collection.places[int(button.id)].name}. Get going!"
            else:
                message.text = f"You need to visit {self.collection.places[int(button.id)].name}."
        else:
            if self.collection.places[int(button.id)].isImp() == True:
                message.text = f"You visited {self.collection.places[int(button.id)].name}. Great travelling!"
            else:
                message.text = f"You visited {self.collection.places[int(button.id)].name}."

        self.build_places() 

    def on_sort(button):
        app = App.get_running_app()
        dropdown = app.root.ids.dropdown
        custom = app.root.ids.custom_class
        if button.text == "visited":
            custom.collection.sort("visited")
            dropdown.select("visited")
        elif button.text == "priority":
            custom.collection.sort("priority")
            dropdown.select('priority')
        elif button.text == "name":
            custom.collection.sort("name")
            dropdown.select('name')
        elif button.text == "country":
            custom.collection.sort("country")
            dropdown.select('country')
        custom.build_places()

    def on_add(button):
        app = App.get_running_app()
        custom = app.root.ids.custom_class
        name = app.root.ids.name_input.text.strip()
        country = app.root.ids.country_input.text.strip()
        priority = app.root.ids.priority_input.text.strip()
        message = app.root.ids.message
        # print(name, country, priority)
        if name == "" or country == "" or priority == "":
            message.text = "All fields must be completed"
        else:
            try:
                priority = int(priority)
                if priority <= 0:
                    message.text = "Priority must be > 0"
                else:
                    custom.collection.add_place(Place(name, country, priority))
                    custom.build_places()
            except:
                message.text = "Please enter a valid number"

    def on_clear(button):
        app = App.get_running_app()
        name = app.root.ids.name_input
        country = app.root.ids.country_input
        priority = app.root.ids.priority_input
        message = app.root.ids.message
        name.text = ""
        country.text = ""
        priority.text = ""
        message.text = ""

            
        

if __name__ == '__main__':
    TravelTrackerApp().run()
