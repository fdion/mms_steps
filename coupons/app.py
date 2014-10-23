from flask import Flask, request, render_template, redirect, url_for


twilio_logo_png_url = 'http://www.twilio.com/packages/company/' + \
                      'img/logos_downloadable_logobrand.png'

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

@app.route('/', methods=['GET', 'POST'])
def create_coupon():
    # we'll replace the following line later in the tutorial
    return 'stub'

@app.route('/confirmation/', methods=['GET'])
def coupon_confirmation():
    # we'll replace the following line later in the tutorial
    return 'stub'