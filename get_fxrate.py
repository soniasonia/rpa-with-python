import requests
from lxml import html
from logger import info, error

NBP_URL = 'http://api.nbp.pl/api/exchangerates/rates/c/'
PEKAO_URL = 'https://www.pekao.com.pl/kursy-walut.html'
ING_URL = 'https://www.ing.pl/kursy-walut'
SANTANDER_URL = 'https://santander.pl/przydatne-informacje/kursy-walut/pieniadz/kursy-walut-pieniadz.html'
err_msg = "API request failed. Status code: {}"


def get_fxrates():
    rates = {'NBP': {'EUR': 0.0, 'USD': 0.0},
             'Pekao': {'EUR': 0.0, 'USD': 0.0},
             'ING': {'EUR': 0.0, 'USD': 0.0},
             'Santander': {'EUR': 0.0, 'USD': 0.0},
             }
    info('[FX rates] Downloading rates from web...')
    try:
        response = requests.request('GET', NBP_URL + 'eur/')
        assert response.status_code == 200, err_msg.format(response.status_code)
        rates['NBP']['EUR'] = response.json()['rates'][0]['ask']
        response = requests.request('GET', NBP_URL + 'usd/')
        assert response.status_code == 200, err_msg.format(response.status_code)
        rates['NBP']['USD'] = response.json()['rates'][0]['ask']
    except Exception as e:
        error('(NBP) ' + str(e))

    try:
        response = requests.request('GET', PEKAO_URL)
        assert response.status_code == 200, err_msg.format(response.status_code)
        tree = html.fromstring(response.content)
        results = tree.xpath(
            "//*[contains(text(),'EUR')]/../../..//*[@class='cr-sell no-margin']/span")
        rates['Pekao']['EUR'] = float(results[0].text)
        results = tree.xpath(
            "//*[contains(text(),'USD')]/../../..//*[@class='cr-sell no-margin']/span")
        rates['Pekao']['USD'] = float(results[0].text)
    except Exception as e:
        error("(Pekao) " + str(e))

    try:
        response = requests.request('GET', ING_URL)
        assert response.status_code == 200, err_msg.format(response.status_code)
        tree = html.fromstring(response.content)
        results = tree.xpath("//td[contains(text(),'EUR')]/../td[5]/span")
        rate = results[0].text
        rates['ING']['EUR'] = float(rate.replace(',', '.')[:-4])
        results = tree.xpath(
            "//td[contains(text(),'USD')]/../td[5]/span")
        rate = results[0].text
        rates['ING']['USD'] = float(rate.replace(',', '.')[:-4])
    except Exception as e:
        error('(ING) ' + str(e))

    try:
        response = requests.request('GET', SANTANDER_URL)
        assert response.status_code == 200, err_msg.format(response.status_code)
        tree = html.fromstring(response.content)
        results = tree.xpath(
            "//*[contains(text(),'1 EUR')]/following::td[2]/span")
        rate = results[0].text
        rates['Santander']['EUR'] = float(rate)
        results = tree.xpath(
            "//*[contains(text(),'1 USD')]/following::td[2]/span")
        rate = results[0].text
        rates['Santander']['USD'] = float(rate)
    except Exception as e:
        error('(Santander) ' + str(e))

    return rates


print(get_fxrates())
