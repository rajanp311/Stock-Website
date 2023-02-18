import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        symbol = request.form['symbol']
        api_key = 'YOUR_API_KEY'
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        if 'Error Message' in data:
            error = 'Invalid symbol. Please try again.'
            return render_template('index.html', error=error)
        else:
            dates = []
            prices = []
            for date in data['Time Series (Daily)']:
                dates.append(date)
                prices.append(float(data['Time Series (Daily)'][date]['4. close']))
            return render_template('stock.html', symbol=symbol, dates=dates, prices=prices)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
