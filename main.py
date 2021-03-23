# Kivy
from kivy.app import App
from kivy.lang import Builder
# Kivy MapView stuff
from kivy_garden.mapview import MapView, MapMarkerPopup
# Kivy properties
from kivy.properties import StringProperty

class PointOfInterest():
    def __init__(self, latitude, longitude, title='POI', description=''):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.description = description

class Content(MapView):
    def build(self):
        return self

class SchoolMarkerPopup(MapMarkerPopup):
    marker = 'schoolmarker.png'

class MapApp(App):
     def build(self):
         root_widget = Builder.load_file('mapViewGUI.kv')
         root_widget.build()
         mymarker = SchoolMarkerPopup(lat=55.015133314076266, lon=11.916701493737868)
         root_widget.add_marker(mymarker)
         return root_widget

if __name__ in ('__main__', '__android__'):
    MapApp().run()
