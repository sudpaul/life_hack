
import pandas as pd
import folium
from realestate import clean_data

data = pd.reada_csv('./Raw-data/file-name')
data_clean = clean_data(data)

lat = list(data_clean["latitude"])
lon = list(data_clean["longitude"])
price = list(data_clean["price"])

html = """<h4>House Price:</h4>
value: %s m
"""

map = folium.Map(location=[data_clean['latitude'].mean(), data_clean['longtitude'].mean()], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "Real-estate_map")

for lt, ln, el in zip(lat, lon, price):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))


map.add_child(fg)
map.save("Map_html_popup_simple.html")
map

