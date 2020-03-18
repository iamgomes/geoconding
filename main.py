from geocoding import geocoding
from streetview import baixa_imagem
import pandas as pd
import numpy as np

def main():
    geocoding()

    df = np.array(pd.read_csv('locations_kml.csv', header=None))

    baixa_imagem(df[0][2],df[0][3])


if __name__ == "__main__":
    main()