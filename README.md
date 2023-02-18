# Stock-Website
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock/<symbol>')
def stock(symbol):
    api_key = 'YOUR_API_KEY'  # replace this with your actual API key
    url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    stock_data = data['values']

    # extract the dates and closing prices
    dates = [d['datetime'] for d in stock_data]
    prices = [float(d['close']) for d in stock_data]

    return render_template('stock.html', symbol=symbol, dates=dates, prices=prices)

if __name__ == '__main__':
    app.run()
