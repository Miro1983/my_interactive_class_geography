import streamlit as st
import pandas as pd
import requests 
import sqlalchemy as db
#import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import branca
#import os
from pathlib import Path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import streamlit as st

#import logging

import numpy as np
from PIL import Image
import pydeck as pdk
import geopy

engine = create_engine(
    "shillelagh://",
     adapters=["gsheetsapi"],
     adapter_kwargs={
         "gsheetsapi": {
             "service_account_info": {
                 "type": "service_account",
                 "project_id": "hidden-will-368520",
                 "private_key_id": "e0858ae3051e13ab0fa8a2d89e1eecd8a7eebe8b",
                 "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCq94AuGOXhE3lf\nrGEJCIGITC03umixgwKizmOkBSsLzmthnKSzGLFBih2YyYtHtVp3reYOY1qXyngS\nNjGLNN1E9LfauBSULuz/E1QyCEb0/avEN/uRG3QpsCu+zlvR8uYgY2t4uNLQ0rmI\n3JZATCgPUEUdaJ1LL7ouF6aOIwoKCNWtqhB3jUqdXDrlbmKLG9H6mnfTCtem4OUz\n1v1acxfwqo2MAMnixNIYPTO+ByiTecFkHBhTQ/LN76fxLfJRtgZjTS0w1fLkp6MH\nLXkBlH/2wPsL0diok8YEG6jNEwbjJ6eZ+9yEba3e+eIbp2SW4kTQsgNedFgwSNIS\n+zdN4/CVAgMBAAECggEABALl8ARHiH4OJU+Ea1OBbog9sLFf+XeVx+odw7XB/8yV\nD7zpebDvn8EKLBE2gl/f7S+YVpLAMmWJZwFR15lNmRZA0LyW8a8e17vwCB3SRGHw\noMb2Jmka0vY+NdjeUKZpUy3h/KV21M13lZ16AleHF8I4t5WXyIbTJc0KQbV9a896\nwy2T0FqjSRO+UJlgYK3HdzNNcukN9kAq1f0fZNwBEMXdUVMQiQCi9VJIDX9SpqzM\n2x8CJTPF5AKWWym0OHt5EJVffcjjf/M0+Ys7O4Ak4JNpsO7g7jAyrMssbn/4NhzC\n2zkxcM9bAuX8640hPkafJManfZwEaMr8S3Mug7A9oQKBgQDaRzP4+NvtiZpdE3Y6\n2MZC98y0mfEzF+P4Vq7kl5djZKs8xEesBMUbVBd7jeARAdK1K88gJ7SLsXAzcMx4\n9CPumDQZ/47uHMD5UyoaqGK9OGRRWIkc68BzQss6UF97Rj6kqggEktfUoT2tcY8o\nTudbSI3d4dHc7xkW8NWGtul0iQKBgQDIgzTxDEwWz+G2B0vYjRIblYQ78gmucP+9\nuOzRyR5P6lnebaViOe0S83HoZRaV0jq+UUvQrYs5pCjusDUuMZ0oC0nl/jbEREJo\nwnaPAcgzgFNLlAA5QcVcd90TJAIswfxUPZUO0/wZy6MKgloIGn8WeOnjLnfboEuT\nNxnDpXKwrQKBgQDJKlwEtd2CgpGn/Bq3SzcVWujm/QUlEHyCT+kpNWhJKusBuudO\n6qp5cDugG/YH1oVJgRGH0e/72lDMp8VaJ67B4rYJy9P/MLLMVU/1d4BgYQtbSNw8\nsi0QTNudZ5tHskpjWWzAQlD1XpDIO2MzQ9zG7QwKFGdkVVrrIJO5bvOi+QKBgF5t\n7DDZKbxUime/Z+jEBxMWhv/0LLsKXGZtAJqLrMrWAxzNZmWsAgo6vBpGASztpNyc\nTKgqErdCqERAl8r5cpm5N0QpRIGJ4/ySGGOg4zfd51xghvpwDxJNIMAy5RNPCBZk\nKh6hlshPLql0WhIW6GMc7okfCTNVekIKYQfSkwDBAoGAOpE8LY+sBOifg6xjl5ua\nj1l658V4tPOROJ14KjswHS3p4wLxlH7/rj1O7BvJnjQB+oFQPVLuUMHga3oGO4Sl\nP/GIpsgfIBOLenSoEx5nTKCvoiKQK/JH4AurKgKwTY3H5xR9ho5sa/zBsMBryzzB\nT364lLAwBWbVwf6Z7nzj7NM=\n-----END PRIVATE KEY-----\n",
                 "client_email": "drerrrr@hidden-will-368520.iam.gserviceaccount.com",
                 "client_id": "112223709029329197118",
                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                 "token_uri": "https://oauth2.googleapis.com/token",
                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                 "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/drerrrr%40hidden-will-368520.iam.gserviceaccount.com"
            },
             "catalog":
             {
                 "Interactive_class": "https://docs.google.com/spreadsheets/d/12f3o40DyzQpMo2wkbAxqldaA_HI81gk8Md0kJmyN_HE/edit#gid=1747533781"
             }
         },
     },
)

    


gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


st.title('Интерактивна карта')
st.markdown('Това е вашият интерактивен час')
address = st.text_input('Местоположение: ')

base = declarative_base()
class My_object(base):
    __tablename__ = 'Interactive_class'
    #id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    address = Column(String)
    temperature = Column(Integer)
    date = Column(String)


def read_db(Obj):
    mine = sessionmaker(bind=engine)
    session = mine()

    df = pd.read_sql_query(sql = db.select([My_object.name, My_object.address, My_object.temperature, My_object.date,
                                        ]), con=engine)
    return df

options_form2 = st.sidebar.form('options_form2')
option2 = options_form2.radio('Моля изберете къде живеете', ('Сливен', 'Гергевец', 'Камен', 'Крушаре', 'Сотиря', 'Чинтулово'))

def choose_string(option2):
    if option2 == 'Сливен':
        return '1MnLgg3IPC9ImxAc4URmzj4ST_qhg19Xy'
    elif option2 == 'Гергевец':
        return '1ZLqv9Aq14xMK7bn7NP7eK6T1FyfoI4DT'
    elif option2 == 'Камен':
        return '1VJSQSJL5ElijRtNNyYedM0ziHejIzwXm'
    elif option2 == 'Крушаре':
        return '1sJJYT3b2uEFHMIfKikNvhk2q0ZA-mR7E'
    elif option2 == 'Сотиря':
        return '1-Z7dfUaCd4VqHoUUpswohFLwS3Gk379h'
    elif option2 == 'Чинтулово':
        return '1hO7AXY3NfNzT5V6gkJVz9sDl5W3nfmj_'
    
my_drive = choose_string(option2)

# To list all files in your google drive at the root folder
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(my_drive)}).GetList()









img_file_buffer = options_form2.camera_input("Снимай")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    name = options_form2.text_input('Въведете име на снимката')
    im = Image.fromarray(img_array)
    button2 = options_form2.form_submit_button('Зареди снимката')
    if button2 and name is not None:
 
        im.save(f"{name}.jpg")
        image_string = f'{name}.jpg'
        gfile = drive.CreateFile({'parents': [{'id': my_drive}]})
        gfile.SetContentFile(image_string)
        gfile.Upload()
        options_form2.write('Снимката беше успешно заредена!')
options_form2.form_submit_button("Потвърди")

web_links = []
title = []

for file in file_list:
    url = f"https://drive.google.com/uc?export=view&id={file['id']}"
    web_links.append(url)
    title.append(file['title'])

my_dict = {
    'url': web_links,
    'title': title
}

data = pd.DataFrame(my_dict)

thumbnails = []
for index,row in data.iterrows():
    s = row['url']
    thumbnail_url = f"<img src='{s}' width='100px'>"
    thumbnails.append(thumbnail_url)
    
data['thumbnail'] = thumbnails

html = ''
for t in data['thumbnail']:
    html += t


    


def geocode(query):
    d = {'Sliven': (42.6817, 26.3229), 'Сливен': (42.6817, 26.3229), 'Samuilovo': (42.5913, 26.324),
         'Самуилово': (42.5913, 26.324), 'Крушаре': (42.5629, 26.3822), 'Krushare': (42.5629, 26.3822),
         'Чинтулово': (42.6455, 26.2368), 'Сотиря': (42.6909, 26.4035), 'Струпец': (42.6141, 26.1102), 
         'Гергевец': (42.5907, 26.3443)}
    
    if query in d:
        return d[query]
    else:
        locator = geopy.Nominatim(user_agent="myGeocoder")
        location = locator.geocode(query)
        return location[1]
        





options_form1 = st.sidebar.form('options_form1')
name1 = options_form1.text_input('Име')
address1 = options_form1.text_input('Адрес')
temperature1 = options_form1.number_input('Температура', min_value=-20.0, max_value=40.0, step=1.0)
date1 = options_form1.date_input('Дата')

add_data = options_form1.form_submit_button('Потвърди')

mine = sessionmaker(bind=engine)
session = mine()


def send_data(name1, address1, temperature1, date1):
    new_rec = My_object(name=name1, address=address1, temperature=temperature1, date=date1)
    session.add(new_rec)
    session.commit()



if add_data:
    send_data(name1, address1, temperature1, date1)
    options_form1.write('Успешно заредихте данните. Благодаря!')


def add_lat_lng(Obj):
    df = read_db(Obj)
    d = {'Sliven': (42.6817, 26.3229), 'Сливен': (42.6817, 26.3229), 'Samuilovo': (42.5913, 26.324),
         'Самуилово': (42.5913, 26.324), 'Крушаре': (42.5629, 26.3822), 'Krushare': (42.5629, 26.3822),
         'Чинтулово': (42.6455, 26.2368), 'Сотиря': (42.6909, 26.4035), 'Струпец': (42.6141, 26.1102), 
         'Гергевец': (42.5907, 26.3443)}
    df['latitude'] = None
    df['longitude'] = None
    for i, row in enumerate(df['address']):
        if row in d:
            df['latitude'][i] = d[row][0]
            df['longitude'][i] = d[row][1]
        else:
            df.drop(i, axis=0, inplace=True)
            
    return df





option1 = st.radio('Моля изберете една от следните опции', ('Карта - сателитно изображение', 'Карта - резултати'))

if option1 == 'Карта - сателитно изображение' and address:
    html = html
    result = geocode(address)
    m = leafmap.Map(location=result, layers_control=True, draw_control=False, measure_control=True, fullscreen_control=True, zoom=10)
    m.add_basemap("HYBRID")
    iframe = leafmap.folium.IFrame(html=html, width=500, height=300)
    popup = leafmap.folium.Popup(iframe, max_width=2650)
    m.add_marker(location=result, popup=popup)
    m_streamlit = m.to_streamlit(800, 800)
elif option1 == 'Карта - резултати':
    df = add_lat_lng(My_object)
    my_df = df[['temperature', 'latitude', 'longitude']]
    
    view = pdk.data_utils.compute_view(df[["longitude", "latitude"]])
    view.pitch = 75
    view.bearing = 60

    token = 'pk.eyJ1IjoibWlyb3NsYXY4MyIsImEiOiJjbGZoOWp3aXQzZ3lqM3NwYzhoMXB2NGFiIn0.CxXFlomYZssLjf3AkXp7nw'

    st.pydeck_chart(pdk.Deck( 
                             initial_view_state=view,
                             api_keys={'mapbox': token},
                             map_provider="mapbox",
                             map_style=pdk.map_styles.SATELLITE,
                             tooltip = {"html": "<b>Брой наблюдения:</b> {elevationValue}","style": {"backgroundColor": "steelblue","color": "white"}},
                             layers=[pdk.Layer("HexagonLayer",
                                               data=my_df,
                                               get_position=["longitude", "latitude"],
                                               auto_highlight=True,
                                               elevation_scale=10,
                                               pickable=True,
                                               elevation_range=[0, 500],
                                               extruded=True,
                                               coverage=1,)]))


