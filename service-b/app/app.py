"""Application main app."""

from flask import Flask, request, send_from_directory
import requests
import logging, coloredlogs

app = Flask(__name__, static_url_path='')

@app.route('/')
def echo_is_alive():
    service_name = 'Service B'
    return f'{service_name} is Alive!'

@app.route('/price')
def get_price():
    api_endpoint = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(api_endpoint)
    price = response.json()
    return(price)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
