import pandas as pd
import numpy as np
from numpy.random import randn
import googlemaps

def geocoding():
    #df = pd.read_csv('locations.csv')
    address = str(input('Digite o endereço a ser pesquisado: '))

    gmaps_key = googlemaps.Client(key='AIzaSyD7UQhpKiSnh__L-bj80sn0I9ws4KDxn08')

    df = pd.DataFrame(randn(1,1), columns=['Endereço'])
    df['Endereço'] = address
    df['LAT'] = None
    df['LON'] = None

    for i in range(len(df)):
        geocode_result = gmaps_key.geocode(df.loc[i,'Endereço'])
        try:
            lat = geocode_result[0]['geometry']['location']['lat']
            lon = geocode_result[0]['geometry']['location']['lng']
            df.loc[i,'LAT'] = lat
            df.loc[i,'LON'] = lon
        except:
            lat = None
            lon = None

    file_name = 'locations_kml.csv'
    df.to_csv(file_name, header=False) #Salva o resultado em csv sem cabeçalho

    print('Arquivo {} gerado com sucesso!'.format(file_name))