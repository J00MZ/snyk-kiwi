"""Application main app."""

from flask import Flask, request, send_from_directory
import requests
import logging, coloredlogs

app = Flask(__name__, static_url_path='')
coloredlogs.install(level='DEBUG', isatty=True)
logger = logging.getLogger('app_log')

@app.route('/')
def echo_is_alive():
    service_name = 'Service A'
    return f'{service_name} is Alive!'

@app.route('/rate')
def get_price():
    api_endpoint = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(api_endpoint)
    all_rates = response.json()
    logger.debug(all_rates)
    usd_rate = all_rates['bpi']['USD']['rate']
    return(usd_rate)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
