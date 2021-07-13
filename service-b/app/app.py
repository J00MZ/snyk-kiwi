"""Application main app."""

from flask import Flask, request, send_from_directory
import requests
import logging, coloredlogs

app = Flask(__name__, static_url_path='')
coloredlogs.install(level='DEBUG', isatty=True)
logger = logging.getLogger('app_log')

def redirect_to_service_a():
    will_redirect = "Hi, I'm Service B! redirecting to service A."
    logger.debug(will_redirect)
    # TODO implement redirect to service here
    return(will_redirect)

@app.route('/')
@app.route('/<request>')
def echo_nothing_here(request):
    if request != 'rate':
        return 'nothing here'
    else:
        return(redirect_to_service_a())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
