from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_zipcode_numbers', methods=['GET'])
def get_zipcode_numbers():
    response = jsonify({
        'zipcode': util.get_zipcode_numbers()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft_living = float(request.form['sqft_living'])
    zipcode = request.form['zipcode']
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(zipcode,sqft_living,bedrooms,bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()