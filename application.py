from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/offer.html')
def offer():
    country = request.args.get('dest')
    return render_template('offer.html', country = country )

@application.route('/booking.html')
def booking():
    country = request.args.get('dest')
    return render_template('booking.html', country = country)


@application.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    application.run()

