
from db_input_management import *

import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
    
root = tk.Tk()
root.title('Meteorological charts')
root.columnconfigure(0, weight=1)

ttk.Label(
  root,
  text="Meteorological charts",
  font=("TkDefaultFont", 16)
).grid()

# Day or night setting frame

dn_info = ttk.LabelFrame(root, text='Day or night setting')
dn_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  dn_info.columnconfigure(i, weight=1 )

dn_radiobutton_value = tk.StringVar()
ttk.Label(dn_info , text='Select day or night data').grid(row=0, column=0)
labframe = ttk.Frame(dn_info)
for lab in ('Day', 'Night'):
  ttk.Radiobutton(
    labframe, value=lab, text=lab, variable=dn_radiobutton_value
).pack(side=tk.LEFT, expand=True)
labframe.grid(row=1, column=0, sticky=(tk.W + tk.E))

# Location setting frame

l_info = ttk.LabelFrame(root, text='Location setting')
l_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  l_info.columnconfigure(i, weight=1 )


location_radiobutton_value = tk.StringVar()
ttk.Label(l_info , text='Select a location').grid(row=0, column=0)
labframe = ttk.Frame(l_info )
for lab in ('Vienna', 'Athens', 'Helsinki'):
  ttk.Radiobutton(
    labframe, value=lab, text=lab, variable=location_radiobutton_value
).pack(side=tk.LEFT, expand=True)
labframe.grid(row=1, column=0, sticky=(tk.W + tk.E))

# Meteorological data setting frame

buttons = ttk.LabelFrame(root, text='Meteorological data types')
buttons.grid(sticky=(tk.W + tk.E))
for i in range(3):
  buttons.columnconfigure(i, weight=1 )

data_types = ["Temperature","Wind speed and direction","Humidity and precipitation","Pressure and radiation"]

data_type_value = tk.StringVar()
ttk.Label(buttons, text='Select data type').grid(row=2, column=0, sticky=(tk.W + tk.E))
ttk.Combobox(
  buttons,
  textvariable=data_type_value,
  values=data_types
).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Reload button frame

reload_button_frame = ttk.LabelFrame(root, text='Reload button')
reload_button_frame.grid(sticky=(tk.W + tk.E))
for i in range(3):
  reload_button_frame.columnconfigure(i, weight=1 )

ttk.Label(reload_button_frame , text='Click Reload button to refresh chart after setting changes').pack(side=tk.TOP)
Reload_button = ttk.Button(reload_button_frame, text='RELOAD')
Reload_button.pack(side=tk.LEFT)

def on_reset():

	day_or_night_field_value = dn_radiobutton_value.get()
	location_radiobutton_field_value = location_radiobutton_value.get()
	data_type_field_value = data_type_value.get()

	title = data_type_field_value  + " - " + location_radiobutton_field_value + " - " + day_or_night_field_value + " - Changes for last 10 days" 

	temperature_series = select_last_10_temperature_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	wind_speed_series = select_last_10_wind_speed_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	wind_direction_series = select_last_10_Wind_direction_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	relative_humidity_series = select_last_10_Relative_humidity_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	total_precipitation_series = select_last_10_Total_precipitation_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	pressure_series = select_last_10_Pressure_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	solar_series = select_last_10_Solar_radiation_intensity_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night_field_value,location_radiobutton_field_value)

	Temperature = {'Temperature': temperature_series}

	Wind_data = {'Wind speed': wind_speed_series, 'Wind direction': wind_direction_series}
	
	Humidity_and_precipitation = {'Relative humidity': relative_humidity_series, 'Total precipitation': total_precipitation_series}
	
	Pressure_and_radiation = {'Pressure': pressure_series, 'Solar radiation intensity': solar_series}

	if data_type_field_value == "Temperature":

		Graph(root, title=title, width=200, dataseries = Temperature).grid(row=20, column=0)

	elif data_type_field_value == "Wind speed and direction":

		Graph(root, title=title, width=200, dataseries = Wind_data).grid(row=20, column=0)

	elif data_type_field_value == "Humidity and precipitation":

		Graph(root, title=title, width=200, dataseries = Humidity_and_precipitation).grid(row=20, column=0)

	elif data_type_field_value == "Pressure and radiation":

		Graph(root, title=title, width=200, dataseries = Pressure_and_radiation).grid(row=20, column=0)

Reload_button.configure(command=on_reset)

Temperature_initial_series = {'Temperature': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

class Graph(tk.Frame):
    def __init__(self, master=None, title="", dataseries="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.fig = Figure(figsize=(8, 4))   # figure dimension
        ax = self.fig.add_subplot(111)
        df = pd.DataFrame(data=dataseries) 
        df.plot(ax=ax)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        tk.Label(self, text=f"{title}").grid(row=0)
        self.canvas.get_tk_widget().grid(row=1, sticky="nesw")
        toolbar_frame = tk.Frame(self)
        toolbar_frame.grid(row=2, sticky="ew")
        NavigationToolbar2Tk(self.canvas, toolbar_frame)
    
Graph(root, title="Please choose the data settings and than click Reload button", width=200, dataseries = Temperature_initial_series).grid(row=20, column=0)

root.mainloop()














































































































