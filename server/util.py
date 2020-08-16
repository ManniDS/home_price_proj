import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(zipcode,sqft,bed,bath):
    try:
        loc_index = __data_columns.index(zipcode.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bed
    x[2] = bath
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bed, bath

    global __model
    if __model is None:
        with open('./artifacts/King_County_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_zipcode_numbers():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_zipcode_numbers())
    print(get_estimated_price('98028',1000,2,1))
    print(get_estimated_price('98028',1000,3,2))
    print(get_estimated_price('98008', 1000, 3, 3)) # other zipcode
    print(get_estimated_price('98034', 1000, 3, 3))  # other zipcode