import sys
import requests

# endpoint_url = "http://sam-user-activity.eu-west-1.elasicbeanstalk.com"

def fetch_data(url):
    try:
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout as err:
        sys.exit('Timeout: ' + err.__str__())
    except requests.exceptions.URLRequired as err:
        sys.exit('URLRequired: ', err)
    except requests.exceptions.ConnectionError as err:
        sys.exit('Connection Error: ' + err.__str__())
    except requests.exceptions.HTTPError as err:
        sys.exit('HTTPError: ' + err.__str__())
    except requests.exceptions.InvalidURL as err:
        sys.exit('InvalidURL: ' + err.__str__())
    except requests.exceptions.TooManyRedirects as err:
        sys.exit('Too Many Redirects: ' + err.__str__())
    except requests.exceptions.RequestException as err:
        sys.exit('Request Exception: ' + err.__str__())

def main(endpoint_url):
    res = fetch_data(endpoint_url)
    return res.json()
