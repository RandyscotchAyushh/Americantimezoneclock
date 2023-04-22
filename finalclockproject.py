from tkinter import *
from tkinter.ttk import *
import datetime
import pytz
import pandas as pd
import folium
import os
import webbrowser

timez = {"Eastern Time": "US/Eastern",
         "Central Time": "US/Central",
         "Mountain Time": "US/Mountain",
         "Pacific Time": "US/Pacific",
         "Alaska Time": "US/Alaska",
         "Hawaii-Aleutian Time": "US/Hawaii",
         "Samoa Time": "Pacific/Samoa"}

eastern_states = {"Alabama": (32.3182, -86.9023),
                  "Connecticut": (41.6032, -73.0877),
                  "Delaware": (38.9108, -75.5277),
                  "Florida": (27.6648, -81.5158),
                  "Georgia": (32.1656, -82.9001),
                  "Indiana": (39.7684, -86.1581),
                  "Kentucky": (37.8393, -84.2700),
                  "Maine": (45.2538, -69.4455),
                  "Maryland": (39.0458, -76.6413),
                  "Massachusetts": (42.4072, -71.3824),
                  "Michigan": (44.3148, -85.6024),
                  "New Hampshire": (43.4525, -71.5639),
                  "New Jersey": (40.0583, -74.4057),
                  "New York": (42.1657, -74.9481),
                  "North Carolina": (35.7596, -79.0193),
                  "Ohio": (40.4173, -82.9071),
                  "Pennsylvania": (41.2033, -77.1945),
                  "Rhode Island": (41.5801, -71.4774),
                  "South Carolina": (33.8361, -81.1637),
                  "Tennessee": (35.5175, -86.5804),
                  "Vermont": (44.5588, -72.5778),
                  "Virginia": (37.4316, -78.6569),
                  "West Virginia": (38.5976, -80.4549)}

pacific_states = {"California": (37.2719, -119.2702),
                  "Oregon": (43.8041, -120.5542),
                  "Washington": (47.7511, -120.7401),
                  "Nevada": (39.5501, -116.7500)}

central_states = {"North Dakota": (47.5515, -101.0020),
                  "South Dakota": (43.9695, -99.9018),
                  "Nebraska": (41.4925, -99.9018),
                  "Kansas": (38.4987, -98.3201),
                  "Oklahoma": (35.0078, -97.0929),
                  "Texas": (31.9686, -99.9018),
                  "Minnesota": (46.7296, -94.6859),
                  "Iowa": (41.8780, -93.0977),
                  "Missouri": (37.9643, -91.8318),
                  "Arkansas": (34.7465, -92.2896),
                  "Louisiana": (31.2448, -92.1450),
                  "Mississippi": (32.3547, -89.3985),
                  "Alabama": (32.3182, -86.9023),
                  "Tennessee": (35.5175, -86.5804),
                  "Wisconsin": (44.5, -89.5),
                  "Illinois": (40.6331 ,-89.3985)}

Mountain_states = {"Arizona": (34.0489, -111.0937),
                   "Colorado": (39.1130, -105.3589),
                   "Idaho": (44.0682, -114.7420),
                   "Montana": (46.8797, -110.3626),
                   "New Mexico": (34.5199, -105.8701),
                   "Utah": (39.3200, -111.0937),
                   "Wyoming": (43.0750, -107.2903)}

us_samoa_time = {"American samoa" : (-14.2710, -170.1322)}
                                       
Hawaii_time = {"Hawaii": (19.741755, -155.844437)}

Alaska_time = {"Alaska": (66.160507, -153.369141)}
               
                



eastern_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

root = Tk()
root.title("Current Time in US Time Zones")

timelabel = Label(root, font=("Arial", 24), foreground="blue")
timelabel.pack()

def update_time():
    current_str = ""
    for tz_name, tz_code in timez.items():
        tz1 = pytz.timezone(tz_code)
        tz2 = datetime.datetime.now(tz1)
        tz3 = tz2.strftime("%Y-%m-%d %H:%M:%S")

        current_str += "{}: {}\n".format(tz_name, tz3)

    timelabel.config(text=current_str)
    timelabel.after(1000, update_time)

update_time()

for city, eastern_states in eastern_states.items():
    label = folium.Popup(city + ": Eastern Time Zone")
    folium.Marker(location=eastern_states, popup=label).add_to(eastern_map)

for city, pacific_states in pacific_states.items():
    label = folium.Popup(city + ": Pacific Time Zone")
    folium.Marker(location=pacific_states, popup=label, icon=folium.Icon(color='red')).add_to(eastern_map)

for city, central_states in central_states.items():
    label = folium.Popup(city + ": Central Time Zone")
    folium.Marker(location=central_states, popup=label, icon=folium.Icon(color='green')).add_to(eastern_map)

for city, Mountain_states in Mountain_states.items():
    label = folium.Popup(city + ": Mountain Time Zone")
    folium.Marker(location=Mountain_states, popup=label, icon=folium.Icon(color='orange')).add_to(eastern_map)

for city, Alaska_time in Alaska_time.items():
    label = folium.Popup(city + ": Alaska Time Zone")
    folium.Marker(location=Alaska_time, popup=label, icon=folium.Icon(color='gray')).add_to(eastern_map)

for city, Hawaii_time in Hawaii_time.items():
    label = folium.Popup(city + ": Pacific Time Zone")
    folium.Marker(location=Hawaii_time, popup=label, icon=folium.Icon(color='pink')).add_to(eastern_map)

for city, us_samoa_time in us_samoa_time.items():
    label = folium.Popup(city + ": Pacific Time Zone")
    folium.Marker(location=us_samoa_time, popup=label, icon=folium.Icon(color='black')).add_to(eastern_map)
eastern_map.save("American_time_zones.html")


webbrowser.open('file://' + os.path.realpath("American_time_zones.html"))

root.mainloop()
       
