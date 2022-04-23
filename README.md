This desktop application displayes meteorological data trend changes in forms of charts.
User selects data settings and click "Reload" buton.
Charts with requested data are displayed.

Prerequisites:

-Python 3.9.7

-tkinter

-pyodbc

-pandas

The database:

CREATE TABLE [dbo].[Weather_Info]( 
[Date] [date] NOT NULL,
[Temperature] [int] NOT NULL,
[Wind_speed] [int] NOT NULL, 
[Wind_direction] [int] NOT NULL,
[Relative_humidity] [int] NOT NULL,
[Total_precipitation] [int] NOT NULL,
[Pressure] [int] NOT NULL,
[Solar_radiation_intensity] [int] NOT NULL,
[Location] varchar(50) NOT NULL,
[Day_or_night] varchar(50) NOT NULL
)

How to run:
python meteo_chart_displayer.py




![app1](https://user-images.githubusercontent.com/89083426/164944717-38cd0d57-8399-4645-97f7-71cc823a2890.png)

![app2](https://user-images.githubusercontent.com/89083426/164944719-5f169ed5-62bf-455b-a48c-3f4135c7b080.png)



