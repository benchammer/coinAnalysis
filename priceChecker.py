import json, requests, math

# C:\Users\CowsillB\PycharmProjects\coinAnalysis\venv\Scripts
# pip3 install requests

url = 'https://api.coinmarketcap.com/v1/ticker/'

# List containing coins of interest
coins = ['ripple','cardano','bitcoin']

# Alert if price has risen or fallen beyond threshold
def alert(metric):
    threshold = 10
    magMetric = float(metric)
    if math.fabs(magMetric) > 25:
        print('!!!ALERT!!!')


# Download the JSON data from https://coinmarketcap.com/api/
def getJSON(a):
    targetURL = url + a + '/'
    response = requests.get(targetURL)
    return response

# Print the price info
def pricePrint(p):
    print(p['name'] + ', ' + p['symbol'])
    print('Price: $' + p['price_usd'])
    print('Percent change today: ' + p['percent_change_24h'] + '%')
    alert(p['percent_change_24h'])
    print('Percent change this week: ' + p['percent_change_7d'] + '% \n')

# Main loop
for coin in coins:
    response = getJSON(coin)
    priceInfo = json.loads(response.text)
    p = priceInfo[0]
    pricePrint(p)