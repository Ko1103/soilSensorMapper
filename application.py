from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')

@application.route('/sesor')
def sensor():
    return render_template('sensor.html')
