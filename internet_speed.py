import speedtest
import urllib
from urllib.request import urlopen


def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False


def speed_test():
    test = speedtest.Speedtest()
    print("-" * 100)
    config = test.get_config()
    fetch_client = config.get('client')
    print("*" * 32 + " INTERNET SERVICE PROVIDER DETAILS  " + "*" * 32)
    print("-" * 100)
    print('ISP IP Address : ' + str(fetch_client.get('ip')))
    print('ISP Name       : ' + fetch_client.get('isp'))
    print('ISP Rating     : ' + str(fetch_client.get('isprating')) + '/5')
    print("-" * 100)
    host = test.get_best_server()
    print("*" * 43 + " HOST DETAILS " + "*" * 43)
    print("-" * 100)
    print('Connected Host : ' + host.get('host'))
    print('Host Name      : ' + host.get('sponsor'))
    print('Host URL       : ' + host.get('url'))
    print('Host Latency   : ' + str(host.get('latency')) + ' ms')
    print('Host Location  : ' + host.get('name') + ',' + host.get('country'))
    print("-" * 100)
    print('Checking Upload Speed ............')
    upload = float(test.upload() / 1000000)
    print(f'Upload Speed : ' + str(round(upload, 2)) + f'Mbps\n')
    print('Checking Download Speed ..........')
    download = float(test.download() / 1000000)
    print(f'Download Speed : ' + str(round(download, 2)) + 'Mbps')
    print("-" * 100)


if is_internet():
    print("Internet Connection is Active")
    speed_test()
else:
    print('Internet is Disconnected ')
