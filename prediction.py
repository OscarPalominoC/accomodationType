# Cargando el modelo
from keras.models import load_model
import pandas as pd


def predict(data):
    """
    The data that we need to enter into this function has to be on this same order
    days_of_stay, genre, age, kids, Accomodation code.
    This function returns a string, and it determines if the accomodation type is either Hotel or AirBnB.
    """
    model = load_model('prediction_model.h5', compile=True)

    country_list = ['AR', 'CO', 'ES', 'IT', 'NL', 'PE', 'UK', 'US']
    array = []
    for value in data:
        if value != data[-1]:
            array.append(int(value))
        else:
            for country in country_list:
                if data[-1] != country:
                    array.append(0)
                else:
                    array.append(1)
    
    result = model.predict(pd.DataFrame(array).T)
    
    if result <= 0.5:
        return 'Hotel'
    else:
        return 'AirBnB'