import google_streetview.api
import google_streetview.helpers
import pandas as pd
import numpy as np

def baixa_imagem(lat, lon):

    address = str(lat) + ',' + str(lon)

    # Define parametros para a api do Street View
    apiargs = {
            'size':'640x300', # max 640x640 pixels
            #'location': str(np.array(address[[2,3]])[0]).replace('[','').replace(']','') ,
            #'location':'-15.6236655,-56.05740429999999;46.414382,10.013988;40.720032,-73.988354',
            'location': address,
            #'heading': '270',
            'fov': '120',
            #'pitch': '0',
            'key':'AIzaSyD7UQhpKiSnh__L-bj80sn0I9ws4KDxn08'
            }


    # Pega a lista de todos os seus argumentos com multiplus parâmetros
    api_list = google_streetview.helpers.api_list(apiargs)

    # Cria o objeto results
    results = google_streetview.api.results(api_list)

    # Download das imagens para o diretório
    results.download_links('img_streetview')

    # Salva links
    results.save_links('img_streetview/links.txt')

    print('Imagens salvas com sucesso!')